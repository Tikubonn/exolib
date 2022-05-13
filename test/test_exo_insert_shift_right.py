
from unittest import TestCase 
from exolib import EXO, ObjectNode, PositionRange, InsertionMode

class TestEXOInsertShiftRight (TestCase):

  def test_insert (self): 

    exo = EXO()
    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    exo.insert_object(1, PositionRange(1, 24), objnode1, InsertionMode.SHIFT_RIGHT)
    exo.insert_object(1, PositionRange(1, 24), objnode2, InsertionMode.SHIFT_RIGHT)
    exo.insert_object(1, PositionRange(1, 24), objnode3, InsertionMode.SHIFT_RIGHT)
    objnodes = list(exo.iter_layer_object(1))
    self.assertEqual(len(objnodes), 3)
    self.assertEqual(objnodes[0], objnode1)
    self.assertEqual(objnodes[0].positionrange.start, 1)
    self.assertEqual(objnodes[0].positionrange.end, 24)
    self.assertEqual(objnodes[1], objnode2)
    self.assertEqual(objnodes[1].positionrange.start, 25)
    self.assertEqual(objnodes[1].positionrange.end, 48)
    self.assertEqual(objnodes[2], objnode3)
    self.assertEqual(objnodes[2].positionrange.start, 49)
    self.assertEqual(objnodes[2].positionrange.end, 72)
