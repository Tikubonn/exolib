
from exolib import PositionRange
from unittest import TestCase 

class TestPositionRange (TestCase):

  def test_is_inside (self):
    posrange = PositionRange(1, 3)
    self.assertEqual(posrange.is_inside(0), False)
    self.assertEqual(posrange.is_inside(1), True)
    self.assertEqual(posrange.is_inside(2), True)
    self.assertEqual(posrange.is_inside(3), True)
    self.assertEqual(posrange.is_inside(4), False)

  def test_contains (self):
    posrange = PositionRange(1, 3)
    self.assertEqual(posrange.contains(PositionRange(0, 1)), False)
    self.assertEqual(posrange.contains(PositionRange(1, 2)), True)
    self.assertEqual(posrange.contains(PositionRange(2, 3)), True)
    self.assertEqual(posrange.contains(PositionRange(3, 4)), False)
    self.assertEqual(posrange.contains(PositionRange(1, 3)), True)

  def test_contains_partial_backward (self):
    posrange = PositionRange(1, 3)
    self.assertEqual(posrange.contains_partial_backward(PositionRange(0, 2)), False)
    self.assertEqual(posrange.contains_partial_backward(PositionRange(1, 3)), True)
    self.assertEqual(posrange.contains_partial_backward(PositionRange(2, 4)), True)
    self.assertEqual(posrange.contains_partial_backward(PositionRange(3, 5)), True)
    self.assertEqual(posrange.contains_partial_backward(PositionRange(4, 6)), False)

  def test_contains_partial_forward (self):
    posrange = PositionRange(1, 3)
    self.assertEqual(posrange.contains_partial_forward(PositionRange(-2, 0)), False)
    self.assertEqual(posrange.contains_partial_forward(PositionRange(-1, 1)), True)
    self.assertEqual(posrange.contains_partial_forward(PositionRange(0, 2)), True)
    self.assertEqual(posrange.contains_partial_forward(PositionRange(1, 3)), True)
    self.assertEqual(posrange.contains_partial_forward(PositionRange(2, 4)), False)

  def test_contains_partial (self):
    posrange = PositionRange(1, 3)
    self.assertEqual(posrange.contains_partial(PositionRange(-2, 0)), False)
    self.assertEqual(posrange.contains_partial(PositionRange(-1, 1)), True)
    self.assertEqual(posrange.contains_partial(PositionRange(0, 2)), True)
    self.assertEqual(posrange.contains_partial(PositionRange(1, 3)), True)
    self.assertEqual(posrange.contains_partial(PositionRange(2, 4)), True)
    self.assertEqual(posrange.contains_partial(PositionRange(3, 5)), True)
    self.assertEqual(posrange.contains_partial(PositionRange(4, 6)), False)
