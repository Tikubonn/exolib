
from exofile import String
from .node import Node
from .sectional import Sectional
from .unique_object import UniqueObject

class ObjectParamNode (Node, UniqueObject, Sectional):

  transformation_table = {
    ("_name", "_name"): String,
  }

  def __init__ (self, _name, **params):
    Node.__init__(self)
    UniqueObject.__init__(self)
    Sectional.__init__(self, **params | { "_name": _name })
