
import uuid 
from collections.abc import Hashable

class UniqueObject (Hashable):

  def __init__ (self):
    self._uuid = uuid.uuid4()

  def __hash__ (self):
    return self._uuid.int 
