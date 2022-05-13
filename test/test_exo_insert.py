
from exolib import EXO, ObjectNode, PositionRange, InsertionMode
from unittest import TestCase 

class TestEXOInsert (TestCase):

  def test_reinsert (self):
    
    # 1 [2 3] 4 [5 6] 7 [8 9] => 
    # 4 [5 6] 7 [8 9] 10 [11 12]

    exo = EXO()
    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    exo.insert_object(1, PositionRange(2, 3), objnode1, InsertionMode.NONE)
    exo.insert_object(1, PositionRange(5, 6), objnode2, InsertionMode.NONE)
    exo.insert_object(1, PositionRange(8, 9), objnode3, InsertionMode.NONE)
    exo.insert_object(1, PositionRange(11, 12), objnode1, InsertionMode.NONE) #reinsert
    objnodes = list(exo.iter_layer_object(1))
    self.assertEqual(len(objnodes), 3)
    self.assertEqual(objnodes[0], objnode2)
    self.assertEqual(tuple(objnodes[0].positionrange), (5, 6))
    self.assertEqual(objnodes[1], objnode3)
    self.assertEqual(tuple(objnodes[1].positionrange), (8, 9))
    self.assertEqual(objnodes[2], objnode1)
    self.assertEqual(tuple(objnodes[2].positionrange), (11, 12))

  def test_reinsert2 (self):
    
    # 1 [2 3] 4 [5 6] 7 [8 9] => 
    # [2 3] 4 7 [8 9] 10 [11 12]

    exo = EXO()
    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    exo.insert_object(1, PositionRange(2, 3), objnode1, InsertionMode.NONE)
    exo.insert_object(1, PositionRange(5, 6), objnode2, InsertionMode.NONE)
    exo.insert_object(1, PositionRange(8, 9), objnode3, InsertionMode.NONE)
    exo.insert_object(1, PositionRange(11, 12), objnode2, InsertionMode.NONE) #reinsert
    objnodes = list(exo.iter_layer_object(1))
    self.assertEqual(len(objnodes), 3)
    self.assertEqual(objnodes[0], objnode1)
    self.assertEqual(tuple(objnodes[0].positionrange), (2, 3))
    self.assertEqual(objnodes[1], objnode3)
    self.assertEqual(tuple(objnodes[1].positionrange), (8, 9))
    self.assertEqual(objnodes[2], objnode2)
    self.assertEqual(tuple(objnodes[2].positionrange), (11, 12))

  def test_reinsert3 (self):
    
    # 1 [2 3] 4 [5 6] 7 [8 9] => 
    # [2 3] 4 [5 6] 7 10 [11 12]

    exo = EXO()
    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    exo.insert_object(1, PositionRange(2, 3), objnode1, InsertionMode.NONE)
    exo.insert_object(1, PositionRange(5, 6), objnode2, InsertionMode.NONE)
    exo.insert_object(1, PositionRange(8, 9), objnode3, InsertionMode.NONE)
    exo.insert_object(1, PositionRange(11, 12), objnode3, InsertionMode.NONE) #reinsert
    objnodes = list(exo.iter_layer_object(1))
    self.assertEqual(len(objnodes), 3)
    self.assertEqual(objnodes[0], objnode1)
    self.assertEqual(tuple(objnodes[0].positionrange), (2, 3))
    self.assertEqual(objnodes[1], objnode2)
    self.assertEqual(tuple(objnodes[1].positionrange), (5, 6))
    self.assertEqual(objnodes[2], objnode3)
    self.assertEqual(tuple(objnodes[2].positionrange), (11, 12))
