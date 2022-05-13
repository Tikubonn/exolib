
from exolib import EXO, ObjectNode, PositionRange, InsertionMode
from unittest import TestCase 

class TestObjectNodeMidPoint (TestCase):

  def test_add (self):

    # 1 [2 3] 4 [5 6] 7 [8 9]

    exo = EXO()
    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    exo.insert_object(1, PositionRange(2, 3), objnode1, InsertionMode.NONE)
    exo.insert_object(1, PositionRange(5, 6), objnode2, InsertionMode.NONE)
    exo.insert_object(1, PositionRange(8, 9), objnode3, InsertionMode.NONE)

    ranges = list(objnode1.iter_range())
    self.assertEqual(len(ranges), 1)
    self.assertEqual(tuple(ranges[0]), (2, 3))
    self.assertEqual(tuple(objnode1.positionrange), (2, 3))

    ranges = list(objnode2.iter_range())
    self.assertEqual(len(ranges), 1)
    self.assertEqual(tuple(ranges[0]), (5, 6))
    self.assertEqual(tuple(objnode2.positionrange), (5, 6))

    ranges = list(objnode3.iter_range())
    self.assertEqual(len(ranges), 1)
    self.assertEqual(tuple(ranges[0]), (8, 9))
    self.assertEqual(tuple(objnode3.positionrange), (8, 9))

  def test_add2 (self):

    # 1 [2 | 3] 4 [5 | 6] 7 [8 | 9]

    exo = EXO()
    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    exo.insert_object(1, PositionRange(2, 3), objnode1, InsertionMode.NONE)
    exo.insert_object(1, PositionRange(5, 6), objnode2, InsertionMode.NONE)
    exo.insert_object(1, PositionRange(8, 9), objnode3, InsertionMode.NONE)
    objnode1.add_midpoint(1) 
    objnode2.add_midpoint(1) 
    objnode3.add_midpoint(1) 

    ranges = list(objnode1.iter_range())
    self.assertEqual(len(ranges), 2)
    self.assertEqual(tuple(ranges[0]), (2, 2))
    self.assertEqual(tuple(ranges[1]), (3, 3))
    self.assertEqual(tuple(objnode1.positionrange), (2, 3))

    ranges = list(objnode2.iter_range())
    self.assertEqual(len(ranges), 2)
    self.assertEqual(tuple(ranges[0]), (5, 5))
    self.assertEqual(tuple(ranges[1]), (6, 6))
    self.assertEqual(tuple(objnode2.positionrange), (5, 6))

    ranges = list(objnode3.iter_range())
    self.assertEqual(len(ranges), 2)
    self.assertEqual(tuple(ranges[0]), (8, 8))
    self.assertEqual(tuple(ranges[1]), (9, 9))
    self.assertEqual(tuple(objnode3.positionrange), (8, 9))

  def test_reinsert (self):

    # 1 [2 | 3] 4 [5 | 6] 7 [8 | 9] => 
    # 11 [12 | 13] 14 [15 | 16] 17 [18 | 19] #midpoint追加後Nodeを移動した場合にmidpointsを継承しているか検証します。

    exo = EXO()
    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    exo.insert_object(1, PositionRange(2, 3), objnode1, InsertionMode.NONE)
    exo.insert_object(1, PositionRange(5, 6), objnode2, InsertionMode.NONE)
    exo.insert_object(1, PositionRange(8, 9), objnode3, InsertionMode.NONE)
    objnode1.add_midpoint(1) 
    objnode2.add_midpoint(1) 
    objnode3.add_midpoint(1) 
    exo.insert_object(1, PositionRange(12, 13), objnode1, InsertionMode.NONE)
    exo.insert_object(1, PositionRange(15, 16), objnode2, InsertionMode.NONE)
    exo.insert_object(1, PositionRange(18, 19), objnode3, InsertionMode.NONE)

    ranges = list(objnode1.iter_range())
    self.assertEqual(len(ranges), 2)
    self.assertEqual(tuple(ranges[0]), (12, 12))
    self.assertEqual(tuple(ranges[1]), (13, 13))
    self.assertEqual(tuple(objnode1.positionrange), (12, 13))

    ranges = list(objnode2.iter_range())
    self.assertEqual(len(ranges), 2)
    self.assertEqual(tuple(ranges[0]), (15, 15))
    self.assertEqual(tuple(ranges[1]), (16, 16))
    self.assertEqual(tuple(objnode2.positionrange), (15, 16))

    ranges = list(objnode3.iter_range())
    self.assertEqual(len(ranges), 2)
    self.assertEqual(tuple(ranges[0]), (18, 18))
    self.assertEqual(tuple(ranges[1]), (19, 19))
    self.assertEqual(tuple(objnode3.positionrange), (18, 19))

  def test_reinsert2 (self):

    # 1 [2 | 3] => 11 [12 | 13 23] #midpoint追加後Nodeを移動した場合にmidpointsを継承しているか検証します。

    exo = EXO()
    objnode = ObjectNode()
    exo.insert_object(1, PositionRange(2, 3), objnode, InsertionMode.NONE)
    objnode.add_midpoint(1) 
    exo.insert_object(1, PositionRange(12, 23), objnode, InsertionMode.NONE) 

    ranges = list(objnode.iter_range())
    self.assertEqual(len(ranges), 2)
    self.assertEqual(tuple(ranges[0]), (12, 12))
    self.assertEqual(tuple(ranges[1]), (13, 23))
    self.assertEqual(tuple(objnode.positionrange), (12, 23))

  def test_reinsert3 (self):

    # 11 [12 | 13 23] => 1 [2 | 3] #midpoint追加後Nodeを移動した場合にmidpointsを継承しているか検証します。

    exo = EXO()
    objnode = ObjectNode()
    exo.insert_object(1, PositionRange(12, 23), objnode, InsertionMode.NONE)
    objnode.add_midpoint(1) 
    exo.insert_object(1, PositionRange(2, 3), objnode, InsertionMode.NONE) 

    ranges = list(objnode.iter_range())
    self.assertEqual(len(ranges), 2)
    self.assertEqual(tuple(ranges[0]), (2, 2))
    self.assertEqual(tuple(ranges[1]), (3, 3))
    self.assertEqual(tuple(objnode.positionrange), (2, 3))

  def test_reinsert4 (self):

    # 11 [12 | 22 23] => 1 [2 3] #midpoint追加後Nodeを移動した場合にmidpointsを継承しているか検証します。

    exo = EXO()
    objnode = ObjectNode()
    exo.insert_object(1, PositionRange(12, 23), objnode, InsertionMode.NONE)
    objnode.add_midpoint(10) 
    exo.insert_object(1, PositionRange(2, 3), objnode, InsertionMode.NONE) 

    ranges = list(objnode.iter_range())
    self.assertEqual(len(ranges), 1)
    self.assertEqual(tuple(ranges[0]), (2, 3))
    self.assertEqual(tuple(objnode.positionrange), (2, 3))

  def test_reinsert5 (self):

    # 1 [2 3] => 11 [12 | 22 23] #midpoint追加後Nodeを移動した場合にmidpointsを継承しているか検証します。

    exo = EXO()
    objnode = ObjectNode()
    exo.insert_object(1, PositionRange(2, 3), objnode, InsertionMode.NONE)
    objnode.add_midpoint(11) 
    exo.insert_object(1, PositionRange(12, 23), objnode, InsertionMode.NONE) 

    ranges = list(objnode.iter_range())
    self.assertEqual(len(ranges), 2)
    self.assertEqual(tuple(ranges[0]), (12, 22))
    self.assertEqual(tuple(ranges[1]), (23, 23))
    self.assertEqual(tuple(objnode.positionrange), (12, 23))

  def test_add_error (self):
    objnode = ObjectNode()
    with self.assertRaises(ValueError):
      objnode.add_midpoint(0) #midpoint must be over 1.
    objnode = ObjectNode()
    objnode.add_midpoint(1)
    with self.assertRaises(ValueError):
      objnode.add_midpoint(1) #already exists.

  def test_remove (self):

    # 1 [2 | 3] 4 [5 | 6] 7 [8 | 9]

    exo = EXO()
    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    exo.insert_object(1, PositionRange(2, 3), objnode1, InsertionMode.NONE)
    exo.insert_object(1, PositionRange(5, 6), objnode2, InsertionMode.NONE)
    exo.insert_object(1, PositionRange(8, 9), objnode3, InsertionMode.NONE)
    objnode1.add_midpoint(1) 
    objnode2.add_midpoint(1) 
    objnode3.add_midpoint(1) 
    objnode1.remove_midpoint(1) 
    objnode2.remove_midpoint(1) 
    objnode3.remove_midpoint(1) 

    ranges = list(objnode1.iter_range())
    self.assertEqual(len(ranges), 1)
    self.assertEqual(tuple(ranges[0]), (2, 3))

    ranges = list(objnode2.iter_range())
    self.assertEqual(len(ranges), 1)
    self.assertEqual(tuple(ranges[0]), (5, 6))

    ranges = list(objnode3.iter_range())
    self.assertEqual(len(ranges), 1)
    self.assertEqual(tuple(ranges[0]), (8, 9))
