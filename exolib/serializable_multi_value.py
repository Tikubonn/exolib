
from abc import abstractmethod
from exofile import SerializableValue, TrackBarType, IntTrackBarRange, FloatTrackBarRange, serialize_value

class SerializableMultiValue (SerializableValue):

  @abstractmethod
  def value_at (self, index:int) -> "SerializableValue":
    pass

  @abstractmethod
  def merge (self, serializablemultivalue:"SerializableMultiValue") -> "SerializableMultiValue":
    pass

  def serialize (self) -> str:
    return self.value_at(0).serialize()

def serialize_value_at (value, index):
  if isinstance(value, SerializableMultiValue):
    return value.value_at(index).serialize()
  else:
    return serialize_value(value)

class TrackBarRanges (SerializableMultiValue):

  """
  TrackBarRanges(TrackBarRanges) => copy
  TrackBarRanges(value) => new 
  TrackBarRanges(values, TrackBarType, *, accelerate=False, decelerate=False, parameter=None)
  """

  trackbar_range_type = None 

  def __init__ (self, *args, accelerate=False, decelerate=False, parameter=None):
    if len(args) == 1:
      value, = args 
      if isinstance(value, TrackBarRanges):
        self.values = list(value.values) #cast and copy for avoid side effects.
        self.trackbartype = value.trackbartype
        self.accelerate = value.accelerate
        self.decelerate = value.decelerate
        self.parameter = value.parameter
      else:
        self.values = [ value ]
        self.trackbartype = TrackBarType.NONE
        self.accelerate = accelerate
        self.decelerate = decelerate
        self.parameter = parameter
    elif len(args) == 2:
      values, trackbartype = args 
      if len(values) >= 2:
        self.values = list(values) #cast and copy for avoid side effects.
        self.trackbartype = trackbartype
        self.accelerate = accelerate
        self.decelerate = decelerate
        self.parameter = parameter
      else:
        raise ValueError("First arguments length must be over 2.")
    else:
      raise ValueError("Normal arguments length must be 0 or 1.")

  def value_at (self, index):
    if self.values:
      if len(self.values) == 1:
        return self.trackbar_range_type(self.values[0])
      else:
        ind1 = min(index, len(self.values) -1)
        ind2 = min(index +1, len(self.values) -1)
        return self.trackbar_range_type(
          self.values[ind1], 
          self.values[ind2], 
          self.trackbartype,
          accelerate=self.accelerate, 
          decelerate=self.decelerate, 
          parameter=self.parameter
        )
    else:
      raise ValueError("{}.values is empty.".format(self))

  def merge (self, trackbarranges):
    if (self.trackbartype == trackbarranges.trackbartype and
        self.accelerate == trackbarranges.accelerate and 
        self.decelerate == trackbarranges.decelerate and 
        self.parameter == trackbarranges.parameter):
      if len(self.values) == 1 and len(trackbarranges.values) == 1:
        if self.values[0] == trackbarranges.values[0]:
          return type(self)(self.values[0])
        else:
          raise ValueError()
      elif len(self.values) >= 2 and len(trackbarranges.values) >= 2:
        if (self.trackbartype == TrackBarType.LINEAR or 
            self.trackbartype == TrackBarType.ACCELERATION or  
            self.trackbartype == TrackBarType.CURVE or 
            self.trackbartype == TrackBarType.TELEPORTATION):
          if self.values[-1] == trackbarranges.values[0]:
            return type(self)(
              self.values + trackbarranges.values[1:],
              self.trackbartype,
              accelerate=self.accelerate,
              decelerate=self.decelerate,
              parameter=self.parameter
            )
          else:
            raise ValueError("{} last value and {} first value must be equal.".format(self, trackbarranges)) #error 
        elif (self.trackbartype == TrackBarType.IGNORE_MIDPOINT or
            self.trackbartype == TrackBarType.MOVE_CERTAIN_AMOUNT or
            self.trackbartype == TrackBarType.RANDOM or
            self.trackbartype == TrackBarType.REPETITION):
          if self.values[0] == trackbarranges.values[0] and self.values[1] == trackbarranges.values[1]:
            return type(self)(
              self.values,
              self.trackbartype,
              accelerate=self.accelerate,
              decelerate=self.decelerate,
              parameter=self.parameter
            )
          else:
            raise ValueError("{} values and {} values must be equal.".format(self, trackbarranges)) #error
      else:
        raise ValueError()
    else:
      raise ValueError("Some properties in {} and {} are not equal.".format(self, trackbarranges)) #error 

  @classmethod
  def deserialize (cls, text):
    trackrange = cls.trackbar_range_type.deserialize(text)
    if trackrange.trackbartype == TrackBarType.NONE:
      return cls(trackrange.start)
    else:
      return cls(
        (trackrange.start, trackrange.end), 
        trackrange.trackbartype,
        accelerate=trackrange.accelerate,
        decelerate=trackrange.decelerate,
        parameter=trackrange.parameter
      )

class IntTrackBarRanges (TrackBarRanges):

  trackbar_range_type = IntTrackBarRange

class FloatTrackBarRanges (TrackBarRanges):

  trackbar_range_type = FloatTrackBarRange
