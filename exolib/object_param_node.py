
from exofile import String
from .node import Node
from .sectional import Sectional
from .unique_object import UniqueObject
from .serializable_multi_value import SerializableMultiValue

class ObjectParamNode (Node, UniqueObject, Sectional):

  transformation_table = {
    ("_name", "_name"): String,
  }

  def __init__ (self, *, forward=None, backward=None, parent=None, **params):
    Node.__init__(self, forward=forward, backward=backward, parent=parent)
    UniqueObject.__init__(self)
    Sectional.__init__(self, **params)

  def is_similar (self, oparamnode):
    return self["_name"] == oparamnode["_name"]

  def merge (self, oparamnode):
    mergedparams = dict()
    uncommonkeys = set(self.keys()) ^ set(oparamnode.keys())
    for key in uncommonkeys:
      if key in self and isinstance(self[key], SerializableMultiValue):
        raise ValueError("{} is not {} instance, but key {} is uncommon.".format(self[key], SerializableMultiValue, key)) #error
      if key in oparamnode and isinstance(oparamnode[key], SerializableMultiValue):
        raise ValueError("{} is not {} instance, but key {} is uncommon.".format(oparamnode[key], SerializableMultiValue, key)) #error 
    commonkeys = set(self.keys()) & set(oparamnode.keys())
    for key in commonkeys:
      if isinstance(self[key], SerializableMultiValue):
        if isinstance(oparamnode[key], SerializableMultiValue):
          mergedparams[key] = self[key].merge(oparamnode[key])
        else:
          raise ValueError("{} and {} must be {} instance.".format(self[key], oparamnode[key], SerializableMultiValue)) #error 
    return type(self)(forward=self.forward, backward=self.backward, parent=self.parent, **dict(self, **mergedparams)) #汚いかもしれませんが引数_nameを**params経由で渡しています。
