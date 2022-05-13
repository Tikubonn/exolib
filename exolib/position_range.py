
from collections.abc import Iterable

class PositionRange:

  def __init__ (self, start, end):
    self.start = min(start, end)
    self.end = max(start, end)

  def __eq__ (self, posrange):
    return (
      isinstance(posrange, Iterable) or 
      isinstance(posrange, PositionRange) and 
      tuple(self) == tuple(posrange)
    )

  def __iter__ (self):
    return iter((self.start, self.end))

  def is_inside (self, position):
    return self.start <= position and position <= self.end

  def contains (self, posrange):
    return self.start <= posrange.start and posrange.end <= self.end

  def contains_partial_backward (self, posrange):
    return self.is_inside(posrange.start)

  def contains_partial_forward (self, posrange):
    return self.is_inside(posrange.end)

  def contains_partial (self, posrange):
    return self.contains_partial_backward(posrange) or self.contains_partial_forward(posrange)
