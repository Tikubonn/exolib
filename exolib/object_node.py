
import copy 
import bisect
import itertools 
from enum import IntEnum, auto
from exofile import Boolean
from .node import Node 
from .sectional import Sectional
from .unique_object import UniqueObject
from .position_range import PositionRange

class InsertionMode (IntEnum):

  NONE = 0
  SHIFT_LEFT = auto()
  SHIFT_RIGHT = auto()
  PUSH_LEFT = auto()
  PUSH_RIGHT = auto()
  OVERWRITE = auto()
  DEFAULT = NONE

class InsertionError (Exception):

  pass

class ObjectNode (Node, UniqueObject, Sectional):

  transformation_table = {
    ("overlay", "overlay"): Boolean,
    ("camera", "camera"): Boolean, 
    ("audio", "audio"): Boolean, 
  }

  def __init__ (self, *, overlay=True, camera=False, audio=False, positionrange=None, midpoints=[], objparamnode=None, forward=None, backward=None, parent=None, **params):
    Node.__init__(self, forward=forward, backward=backward, parent=parent)
    UniqueObject.__init__(self)
    Sectional.__init__(self, **params | { "overlay": overlay, "camera": camera, "audio": audio })
    self._positionrange = positionrange
    self._midpoints = list(midpoints)
    self.objparamnode = objparamnode

  @property
  def midpoints (self):
    return copy.copy(self._midpoints)

  @property
  def positionrange (self):
    return copy.copy(self._positionrange)

  #midpoint 

  def iter_range (self):
    midpointstarts = [ self._positionrange.start + midpoint for midpoint in self._midpoints ]
    midpointends = [ self._positionrange.start + midpoint -1 for midpoint in self._midpoints ]
    starts = [ self._positionrange.start ] + [ midpoint for midpoint in midpointstarts if midpoint <= self._positionrange.end ] #start can contains end pos.
    ends = [ midpoint for midpoint in midpointends if midpoint < self._positionrange.end ] + [ self._positionrange.end ]
    return zip(starts, ends)

  def add_midpoint (self, midpoint):
    if 0 < midpoint:
      if midpoint not in self._midpoints:
        bisect.insort(self._midpoints, midpoint)
      else:
        raise ValueError("Argument of midpoint {} is already exists in {}.midpoints.".format(midpoint, self)) #error 
    else:
      raise ValueError("Argument of midpoint {} must be over 1.".format(midpoint)) #error 

  def remove_midpoint (self, midpoint):
    self._midpoints.remove(midpoint)

  #objparam

  def iter_objparam (self):
    for node in self.objparamnode if (self.objparamnode is not None) else []:
      yield node 

  def contains_objparam (self, oparamnode):
    return oparamnode in self.iter_objparam()

  def add_objparam (self, oparamnode) -> None:
    if oparamnode.parent:
      oparamnode.parent.remove_objparam(oparamnode)
    if self.objparamnode is not None:
      self.objparamnode.last().link_forward(oparamnode)
      oparamnode.parent = self 
    else:
      self.objparamnode = oparamnode
      oparamnode.parent = self 

  def remove_objparam (self, oparamnode) -> None:
    for node in self.objparamnode if (self.objparamnode is not None) else []:
      if opnode is oparamnode:
        if opnode is self.objparamnode:
          self.objparamnode = self.objparamnode.backward or self.objparamnode.forward        
        opnode.independent()
        break
    else:
      raise ValueError("Could not find {} in {}.objparamnode".format(oparamnode, self)) #error 

  #insert 

  def find_by_position (self, position):
    for node in self:
      if node._positionrange.is_inside(position):
        return node 
    else:
      return None 

  def find_by_posrange (self, posrange):
    return [ 
      node for node in self 
      if posrange.contains(node._positionrange) or posrange.contains_partial(node._positionrange) 
    ]

  def _find_backward_nearest_by_position (self, position):
    node = self 
    macthednode = None 
    while (node is not None) and (node._positionrange.is_inside(position) or node._positionrange.start <= position):
      macthednode = node 
      node = node.forward
    return macthednode

  def _find_forward_nearest_by_position (self, position):
    node = self
    while node is not None:
      if node._positionrange.is_inside(position) or position <= node._positionrange.start:
        return node
      node = node.forward
    return None

  def _backwards_start_by (self, position):
    return [ 
      node for node in self.last().backwards() 
      if node._positionrange.start <= position or node._positionrange.end <= position 
    ]

  def _forwards_start_by (self, position):
    return [ 
      node for node in self.first().forwards() 
      if node._positionrange.start >= position or node._positionrange.end >= position 
    ]

  def _positionize_shift_left (self, posrange):
    overlappednodes = self.find_by_posrange(posrange)
    if overlappednodes:
      for node in self._backwards_start_by(posrange.end):
        if node.backward is not None:
          margin = node._positionrange.start - node.backward._positionrange.end -1
          if posrange.end - posrange.start +1 <= margin:
            return PositionRange(
              node._positionrange.start - (posrange.end - posrange.start) -1,
              node._positionrange.start -1
            )
        else:
          margin = node._positionrange.start - 1
          if posrange.end - posrange.start +1 <= margin:
            return PositionRange(
              node._positionrange.start - (posrange.end - posrange.start) -1,
              node._positionrange.start -1
            )
      else:
        raise InsertionError("Could not find best insertion position.")
    else:
      return posrange

  def _positionize_shift_right (self, posrange):
    overlappednodes = self.find_by_posrange(posrange)
    if overlappednodes:
      for node in self._forwards_start_by(posrange.start):
        if node.forward is not None:
          margin = node.forward._positionrange.start - node._positionrange.end -1
          if posrange.end - posrange.start +1 <= margin:
            return PositionRange(
              node._positionrange.end +1,
              node._positionrange.end + (posrange.end - posrange.start) +1
            )
        else:
          return PositionRange(
            node._positionrange.end +1,
            node._positionrange.end + (posrange.end - posrange.start) +1
          )
      else:
        return posrange
    else:
      return posrange

  def _calculate_offset_for_push_left (self, posrange):
    foundnodes = self.find_by_posrange(posrange)
    if foundnodes:
      offset = foundnodes[-1]._positionrange.end - posrange.start +1
      return offset
    else:
      return 0

  def _calculate_offset_for_push_right (self, posrange):
    foundnodes = self.find_by_posrange(posrange)
    if foundnodes:
      offset = posrange.end - foundnodes[0]._positionrange.start +1
      return offset
    else:
      return 0

  def _can_preprocess_push_left (self, posrange):
    offset = ObjectNode._calculate_offset_for_push_left(self, posrange)
    firstnode = self.first()
    return offset <= (firstnode._positionrange.start -1)

  def _preprocess_push_left (self, posrange):
    if ObjectNode._can_preprocess_push_left(self, posrange):
      offset = ObjectNode._calculate_offset_for_push_left(self, posrange)
      for node in self._backwards_start_by(posrange.end):
        node._positionrange = PositionRange(
          node._positionrange.start - offset, 
          node._positionrange.end - offset
        )
      return self
    else:
      raise InsertionError()

  def _preprocess_push_right (self, posrange):
    offset = ObjectNode._calculate_offset_for_push_right(self, posrange)
    for node in self._forwards_start_by(posrange.start):
      node._positionrange = PositionRange(
        node._positionrange.start + offset, 
        node._positionrange.end + offset
      )
    return self

  def _preprocess_overwrite (self, posrange):
    modifiednode = self
    for node in self.find_by_posrange(posrange):
      if posrange.contains(node._positionrange):
        if modifiednode is node:
          modifiednode = modifiednode.backward or modifiednode.forward
        node.independent()
      elif posrange.contains_partial_backward(node._positionrange):
        node._positionrange.start = posrange.end +1
      elif posrange.contains_partial_forward(node._positionrange):
        node._positionrange.end = posrange.start -1
    return modifiednode

  @classmethod
  def insert (cls, posrange, objnode, objnodeto, insertionmode):
    node = objnodeto
    prange = posrange
    if insertionmode == InsertionMode.SHIFT_LEFT:
      if node is not None:
        prange = node._positionize_shift_left(prange)
    elif insertionmode == InsertionMode.SHIFT_RIGHT:
      if node is not None:
        prange = node._positionize_shift_right(prange)
    elif insertionmode == InsertionMode.PUSH_LEFT:
      if node is not None:
        node = node._preprocess_push_left(prange)
    elif insertionmode == InsertionMode.PUSH_RIGHT:
      if node is not None:
        node = node._preprocess_push_right(prange)
    elif insertionmode == InsertionMode.OVERWRITE:
      if node is not None:
        node = node._preprocess_overwrite(prange)
    else:
      if node is not None:
        conflictnode = node.find_by_posrange(prange)
        if conflictnode: #重複するときに例外を送出
          raise InsertionError("Insertion place {} is conflicts to {}.".format(tuple(prange), conflictnode)) #error 
    if node is not None:
      foundbackward = node._find_backward_nearest_by_position(prange.start)
      if foundbackward is not None:
        foundbackward.link_forward(objnode)
        objnode._positionrange = prange
        return node.first()
      else:
        node.first().link_backward(objnode)
        objnode._positionrange = prange
        return node.first()
    else:
      objnode._positionrange = prange
      return objnode

  def merge (self, objnode):
    if self._positionrange.end +1 == objnode._positionrange.start:
      positionrange = PositionRange(self._positionrange.start, objnode._positionrange.end)
      midpoints = self._midpoints + [ objnode._positionrange.start - self._positionrange.start ]
      mergedopnodelast = None 
      for oparamnode, oparamnode2 in zip(self.objparamnode, objnode.objparamnode):
        mergedopnd = oparamnode.merge(oparamnode2)
        mergedopnd.independent()
        if mergedopnodelast is not None:
          mergedopnd.link_backward(mergedopnodelast)
        mergedopnodelast = mergedopnd
      mergedopnode = mergedopnodelast.first()
      return ObjectNode(
        positionrange=positionrange,
        midpoints=midpoints,
        objparamnode=mergedopnode,
        forward=self.forward,
        backward=self.backward,
        parent=self.parent,
        **self
      )
    else:
      raise ValueError("{} and {} must be placed on adjacent.".format(self, objnode)) #error
