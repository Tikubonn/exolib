
from exolib import ObjectNode, InsertionError, InsertionMode, PositionRange
from unittest import TestCase 

class TestObjectNodeInsertShiftLeft (TestCase):

  def test_insert_shift_left (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode4 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    with self.assertRaises(InsertionError):
      ObjectNode.insert(PositionRange(1, 2), objnode4, objnode1, InsertionMode.SHIFT_LEFT)

  def test_insert_shift_left2 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode4 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    with self.assertRaises(InsertionError):
      ObjectNode.insert(PositionRange(2, 3), objnode4, objnode1, InsertionMode.SHIFT_LEFT)

  def test_insert_shift_left3 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode4 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    with self.assertRaises(InsertionError):
      ObjectNode.insert(PositionRange(3, 4), objnode4, objnode1, InsertionMode.SHIFT_LEFT)

  def test_insert_shift_left4 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode4 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = ObjectNode.insert(PositionRange(4, 5), objnode4, objnode1, InsertionMode.SHIFT_LEFT)
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 4)
    self.assertEqual(moddedobjnodes[0], objnode1)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(moddedobjnodes[1], objnode4)
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (4, 5))
    self.assertEqual(moddedobjnodes[2], objnode2)
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (6, 7))
    self.assertEqual(moddedobjnodes[3], objnode3)
    self.assertEqual(tuple(moddedobjnodes[3].positionrange), (10, 11))

  def test_insert_shift_left5 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode4 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = ObjectNode.insert(PositionRange(5, 6), objnode4, objnode1, InsertionMode.SHIFT_LEFT)
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 4)
    self.assertEqual(moddedobjnodes[0], objnode1)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(moddedobjnodes[1], objnode4)
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (4, 5))
    self.assertEqual(moddedobjnodes[2], objnode2)
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (6, 7))
    self.assertEqual(moddedobjnodes[3], objnode3)
    self.assertEqual(tuple(moddedobjnodes[3].positionrange), (10, 11))

  def test_insert_shift_left6 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode4 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = ObjectNode.insert(PositionRange(6, 7), objnode4, objnode1, InsertionMode.SHIFT_LEFT)
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 4)
    self.assertEqual(moddedobjnodes[0], objnode1)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(moddedobjnodes[1], objnode4)
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (4, 5))
    self.assertEqual(moddedobjnodes[2], objnode2)
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (6, 7))
    self.assertEqual(moddedobjnodes[3], objnode3)
    self.assertEqual(tuple(moddedobjnodes[3].positionrange), (10, 11))

  def test_insert_shift_left7 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode4 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = ObjectNode.insert(PositionRange(7, 8), objnode4, objnode1, InsertionMode.SHIFT_LEFT)
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 4)
    self.assertEqual(moddedobjnodes[0], objnode1)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(moddedobjnodes[1], objnode4)
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (4, 5))
    self.assertEqual(moddedobjnodes[2], objnode2)
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (6, 7))
    self.assertEqual(moddedobjnodes[3], objnode3)
    self.assertEqual(tuple(moddedobjnodes[3].positionrange), (10, 11))

  def test_insert_shift_left8 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode4 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = ObjectNode.insert(PositionRange(8, 9), objnode4, objnode1, InsertionMode.SHIFT_LEFT)
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 4)
    self.assertEqual(moddedobjnodes[0], objnode1)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(moddedobjnodes[1], objnode2)
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (6, 7))
    self.assertEqual(moddedobjnodes[2], objnode4)
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (8, 9))
    self.assertEqual(moddedobjnodes[3], objnode3)
    self.assertEqual(tuple(moddedobjnodes[3].positionrange), (10, 11))

  def test_insert_shift_left9 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode4 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = ObjectNode.insert(PositionRange(9, 10), objnode4, objnode1, InsertionMode.SHIFT_LEFT)
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 4)
    self.assertEqual(moddedobjnodes[0], objnode1)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(moddedobjnodes[1], objnode2)
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (6, 7))
    self.assertEqual(moddedobjnodes[2], objnode4)
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (8, 9))
    self.assertEqual(moddedobjnodes[3], objnode3)
    self.assertEqual(tuple(moddedobjnodes[3].positionrange), (10, 11))

  def test_insert_shift_left10 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode4 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = ObjectNode.insert(PositionRange(10, 11), objnode4, objnode1, InsertionMode.SHIFT_LEFT)
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 4)
    self.assertEqual(moddedobjnodes[0], objnode1)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(moddedobjnodes[1], objnode2)
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (6, 7))
    self.assertEqual(moddedobjnodes[2], objnode4)
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (8, 9))
    self.assertEqual(moddedobjnodes[3], objnode3)
    self.assertEqual(tuple(moddedobjnodes[3].positionrange), (10, 11))

  def test_insert_shift_left11 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode4 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = ObjectNode.insert(PositionRange(11, 12), objnode4, objnode1, InsertionMode.SHIFT_LEFT)
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 4)
    self.assertEqual(moddedobjnodes[0], objnode1)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(moddedobjnodes[1], objnode2)
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (6, 7))
    self.assertEqual(moddedobjnodes[2], objnode4)
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (8, 9))
    self.assertEqual(moddedobjnodes[3], objnode3)
    self.assertEqual(tuple(moddedobjnodes[3].positionrange), (10, 11))

  def test_insert_shift_left12 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode4 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = ObjectNode.insert(PositionRange(12, 13), objnode4, objnode1, InsertionMode.SHIFT_LEFT)
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 4)
    self.assertEqual(moddedobjnodes[0], objnode1)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(moddedobjnodes[1], objnode2)
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (6, 7))
    self.assertEqual(moddedobjnodes[2], objnode3)
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (10, 11))
    self.assertEqual(moddedobjnodes[3], objnode4)
    self.assertEqual(tuple(moddedobjnodes[3].positionrange), (12, 13))
