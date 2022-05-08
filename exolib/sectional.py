
from exofile import MutableMappingProxyer
from collections.abc import MutableMapping, Mapping

class Sectional (MutableMappingProxyer):

  transformation_table = {}

  def __init__ (self, **params):
    super().__init__()
    self._params = self._casted_params(params)

  def get_proxy_mutable_mapping (self) -> MutableMapping:
    return self._params

  def _casted_params (self, params:Mapping) -> Mapping:
    paramscopy = dict(params)
    for (sername, desername), destype in self.transformation_table.items():
      if desername in paramscopy:
        paramscopy[desername] = destype(paramscopy[desername])
    return paramscopy

  def _serialized_params (self, params:Mapping) -> Mapping:
    paramscopy = dict(params)
    for (sername, desername), destype in self.transformation_table.items():
      if desername in paramscopy:
        paramscopy[sername] = destype(paramscopy[desername])
        if sername != desername:
          del paramscopy[desername]
    return paramscopy

  @classmethod
  def _deserialized_params (cls, params:Mapping) -> Mapping:
    paramscopy = dict(params)
    for (sername, desername), destype in cls.transformation_table.items():
      if sername in paramscopy:
        paramscopy[desername] = destype.deserialize(paramscopy[sername])
        if desername != sername:
          del paramscopy[sername]
    return paramscopy

  def serialize (self) -> Mapping:
    return self._serialized_params(self._params)

  @classmethod
  def deserialize (cls, params:Mapping) -> "SectionNode":
    return cls(**cls._deserialized_params(params))
