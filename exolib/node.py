
from abc import ABC

class Node (ABC):

  def __init__ (self, *, forward=None, backward=None, parent=None):
    self._forward = forward
    self._backward = backward
    self.parent = parent

  @property
  def forward (self): #readonly
    return self._forward

  @property
  def backward (self): #readonly
    return self._backward

  def __iter__ (self):
    yield from self.forwards()

  def forwards (self):
    node = self
    while node is not None:
      yield node 
      node = node._forward

  def backwards (self):
    node = self
    while node is not None:
      yield node 
      node = node._backward

  def independent (self) -> None:
    node1 = self._backward
    node2 = self
    node3 = self._forward
    node2.parent = None 
    if node1 is not None: node1._forward = node3
    if node2 is not None: node2._forward = None
    if node2 is not None: node2._backward = None
    if node3 is not None: node3._backward = node1

  def last (self):
    node = self 
    while (node is not None) and (node._forward is not None):
      node = node._forward
    return node 

  def first (self):
    node = self 
    while (node is not None) and (node._backward is not None):
      node = node._backward
    return node 

  def link_forward (self, node) -> None:
    node1 = self 
    node2 = node
    node3 = self._forward
    if node1 is not None: node1._forward = node2
    if node2 is not None: node2._forward = node3
    if node2 is not None: node2._backward = node1
    if node3 is not None: node3._backward = node2

  def link_backward (self, node) -> None:
    node1 = self
    node2 = node
    node3 = self._backward
    if node1 is not None: node1._backward = node2
    if node2 is not None: node2._backward = node3
    if node2 is not None: node2._forward = node1
    if node3 is not None: node3._forward = node2

  def move_forward (self) -> None:
    node1 = self._backward
    node2 = self._forward
    node3 = self
    node4 = self._forward._forward if self._forward is not None else None 
    if node2 is not None:
      if node1 is not None: node1._forward = node2
      if node2 is not None: node2._forward = node3
      if node2 is not None: node2._backward = node1
      if node3 is not None: node3._forward = node4
      if node3 is not None: node3._backward = node2
      if node4 is not None: node4._backward = node3

  def move_backward (self) -> None:
    node1 = self._forward
    node2 = self._backward
    node3 = self
    node4 = self._backward._backward if self._backward is not None else None 
    if node2 is not None:
      if node1 is not None: node1._backward = node2
      if node2 is not None: node2._backward = node3
      if node2 is not None: node2._forward = node1
      if node3 is not None: node3._backward = node4
      if node3 is not None: node3._forward = node2
      if node4 is not None: node4._forward = node3
