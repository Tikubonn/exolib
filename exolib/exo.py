
from exofile import EXOFile, Serializable, Int, Boolean
from .exoextra import VideoParamNode, StandardDrawingParamNode, ImageParamNode, AudioParamNode, StandardPlayingParamNode, TextParamNode, ShapeParamNode, FrameBufferParamNode, SoundWaveParamNode, SceneParamNode, PreviousObjectParamNode, ExpansionDrawingParamNode, ParticleParamNode
from .sectional import Sectional
from .object_node import ObjectNode, InsertionMode
from .object_param_node import ObjectParamNode
from .position_range import PositionRange
from .serializable_multi_value import SerializableMultiValue

class EXO (Sectional, Serializable):

  transformation_table = {
    ("width", "width"): Int,
    ("height", "height"): Int,
    ("rate", "rate"): Int,
    ("scale", "scale"): Int,
    ("length", "length"): Int,
    ("audio_rate", "audiorate"): Int,
    ("audio_ch", "audioch"): Int,
  }

  deserialize_objparam_table = {
    "動画ファイル": VideoParamNode, 
    "標準描画": StandardDrawingParamNode, 
    "画像ファイル": ImageParamNode, 
    "音声ファイル": AudioParamNode, 
    "標準再生": StandardPlayingParamNode, 
    "テキスト": TextParamNode, 
    "図形": ShapeParamNode, 
    "フレームバッファ": FrameBufferParamNode, 
    "音声波形表示": SoundWaveParamNode, 
    "シーン": SceneParamNode, 
    "直前のオブジェクト": PreviousObjectParamNode, 
    "拡張描画": ExpansionDrawingParamNode, 
    "パーティクル出力": ParticleParamNode, 
  }

  def __init__ (self, *, width=1280, height=720, rate=24, scale=1, length=0, audiorate=44100, audioch=2, **params):
    super().__init__(**params | { "width": width, "height": height, "rate": rate, "scale": scale, "length": length, "audiorate": audiorate, "audioch": audioch })
    self._layer = [ None ] * 99
    self._layerlookup = {}

  #object

  def iter_object (self):
    for objnode in self._layer:
      for node in objnode or []:
        yield node

  def iter_layer_object (self, layer):
    for node in self._layer[layer -1] or []:
      yield node

  def contains_object (self, objnode):
    return objnode in self.iter_object()

  def contains_layer_object (self, layer, objnode):
    return objnode in self.iter_layer_object(layer)

  def insert_object (self, layer, posrange, objnode, insertionmode=InsertionMode.DEFAULT):
    if objnode.parent:
      objnode.parent.remove_object(objnode)
    self._layer[layer -1] = ObjectNode.insert(posrange, objnode, self._layer[layer -1], insertionmode)
    self._layerlookup[objnode] = layer
    objnode.parent = self 

  def remove_object (self, objnode):
    if objnode in self._layerlookup:
      layer = self._layerlookup[objnode]
      for node in self._layer[layer -1] or []:
        if node is objnode:
          if node is self._layer[layer -1]:
            self._layer[layer -1] = self._layer[layer -1].backward or self._layer[layer -1].forward
          node.independent()
          del self._layerlookup[node]
          break
      else:
        raise ValueError("Could not find {} on layer {:d} in {}.".format(objnode, layer, self))
    else:
      raise ValueError("Could not find {} in {}.".format(objnode, self))

  def find_by_position (self, layer, position):
    if self._layer[layer -1]:
      return self._layer[layer -1].find_by_position(position)
    else:
      return None 

  def find_by_posrange (self, layer, posrange):
    if self._layer[layer -1]:
      return self._layer[layer -1].find_by_posrange(posrange)
    else:
      return []

  def get_object_layer (self, objnode):
    if objnode in self._layerlookup:
      return self._layerlookup[objnode]
    else:
      raise ValueError("Could not find {} in {}.".format(objnode, self))

  def fit_length_to_last_object (self):
    maxend = max(( objnode.positionrange.end for objnode in self.iter_object() ), default=0)
    self["length"] = maxend

  #serializable

  @classmethod
  def load (cls, stream):
    exofile = EXOFile.load(stream)
    exo = EXO.deserialize(exofile["exedit"])
    lastobjnode = None 
    for objnodeid, objparamnodeids in exofile.get_object_section_ids().items():
      objnode = ObjectNode.deserialize(exofile[objnodeid])
      objnodestart = int(objnode["start"])
      objnodeend = int(objnode["end"])
      objnodelayer = int(objnode["layer"])
      objnodechain = objnode.get("chain", False)
      del objnode["start"]
      del objnode["end"]
      del objnode["layer"]
      if objnodechain: del objnode["chain"]
      objnodeposrange = PositionRange(objnodestart, objnodeend)
      exo.insert_object(objnodelayer, objnodeposrange, objnode, InsertionMode.DEFAULT)
      for objparamnodeid in objparamnodeids:
        objparamnodename = exofile[objparamnodeid]["_name"]
        del exofile[objparamnodeid]["_name"]
        objparamnodeclss = cls.deserialize_objparam_table.get(objparamnodename, ObjectParamNode)
        objparamnode = objparamnodeclss.deserialize(exofile[objparamnodeid])
        objnode.add_objparam(objparamnode)
      if objnodechain:
        if lastobjnode is not None:
          mergedobjnode = lastobjnode.merge(objnode)
          mergedobjnodeposrange = mergedobjnode.positionrange
          mergedobjnode.independent()
          lastobjnode.parent.remove_object(lastobjnode) #remove previous node.
          objnode.parent.remove_object(objnode) #remove self.
          exo.insert_object(objnodelayer, mergedobjnodeposrange, mergedobjnode, InsertionMode.DEFAULT)
        else:
          raise ValueError("{} has no previous object.".format(objnode)) #error 
      lastobjnode = objnode
    return exo

  def dump (self, stream):
    exofile = EXOFile()    
    for key, value in self.serialize().items():
      exofile.set("exedit", key, value)
    objectid = 0
    for layerid, objnode in enumerate(self._layer, 1):
      for node in objnode or []:
        for rngeindex, rnge in enumerate(node.iter_range()):
          start, end = rnge
          sectionid = "{:d}".format(objectid)
          if 0 < rngeindex:
            exofile.set(sectionid, "chain", Boolean(True))
          exofile.set(sectionid, "layer", Int(layerid))
          exofile.set(sectionid, "start", Int(start))
          exofile.set(sectionid, "end", Int(end))
          for key, value in node.serialize().items():
            if isinstance(value, SerializableMultiValue):
              atvalue = value.value_at(rngeindex)
            else:
              atvalue = value 
            exofile.set(sectionid, key, atvalue)
          for objparamnodeid, objparamnode in enumerate(node.iter_objparam()):
            sectionid = "{:d}.{:d}".format(objectid, objparamnodeid)
            for key, value in objparamnode.serialize().items():
              if isinstance(value, SerializableMultiValue):
                atvalue = value.value_at(rngeindex)
              else:
                atvalue = value 
              exofile.set(sectionid, key, atvalue)
          objectid += 1
    return exofile.dump(stream)
