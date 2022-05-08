
from exolib import ObjectNode, InsertionError, InsertionMode, PositionRange
from unittest import TestCase 

class TestObjectNodeInsertOverwrite (TestCase):

  def test_insert_overwrite (self):

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
    moddedobjnode = ObjectNode.insert(PositionRange(1, 2), objnode4, objnode1, InsertionMode.OVERWRITE)
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 4)
    self.assertEqual(moddedobjnodes[0], objnode4)
    self.assertEqual(moddedobjnodes[0].positionrange.span(), (1, 2))
    self.assertEqual(moddedobjnodes[1], objnode1)
    self.assertEqual(moddedobjnodes[1].positionrange.span(), (3, 3))
    self.assertEqual(moddedobjnodes[2], objnode2)
    self.assertEqual(moddedobjnodes[2].positionrange.span(), (6, 7))
    self.assertEqual(moddedobjnodes[3], objnode3)
    self.assertEqual(moddedobjnodes[3].positionrange.span(), (10, 11))

  def test_insert_overwrite2 (self):

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
    moddedobjnode = ObjectNode.insert(PositionRange(2, 3), objnode4, objnode1, InsertionMode.OVERWRITE)
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(moddedobjnodes[0], objnode4)
    self.assertEqual(moddedobjnodes[0].positionrange.span(), (2, 3))
    self.assertEqual(moddedobjnodes[1], objnode2)
    self.assertEqual(moddedobjnodes[1].positionrange.span(), (6, 7))
    self.assertEqual(moddedobjnodes[2], objnode3)
    self.assertEqual(moddedobjnodes[2].positionrange.span(), (10, 11))

  def test_insert_overwrite3 (self):

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
    moddedobjnode = ObjectNode.insert(PositionRange(3, 4), objnode4, objnode1, InsertionMode.OVERWRITE)
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 4)
    self.assertEqual(moddedobjnodes[0], objnode1)
    self.assertEqual(moddedobjnodes[0].positionrange.span(), (2, 2))
    self.assertEqual(moddedobjnodes[1], objnode4)
    self.assertEqual(moddedobjnodes[1].positionrange.span(), (3, 4))
    self.assertEqual(moddedobjnodes[2], objnode2)
    self.assertEqual(moddedobjnodes[2].positionrange.span(), (6, 7))
    self.assertEqual(moddedobjnodes[3], objnode3)
    self.assertEqual(moddedobjnodes[3].positionrange.span(), (10, 11))

  def test_insert_overwrite4 (self):

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
    moddedobjnode = ObjectNode.insert(PositionRange(4, 5), objnode4, objnode1, InsertionMode.OVERWRITE)
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 4)
    self.assertEqual(moddedobjnodes[0], objnode1)
    self.assertEqual(moddedobjnodes[0].positionrange.span(), (2, 3))
    self.assertEqual(moddedobjnodes[1], objnode4)
    self.assertEqual(moddedobjnodes[1].positionrange.span(), (4, 5))
    self.assertEqual(moddedobjnodes[2], objnode2)
    self.assertEqual(moddedobjnodes[2].positionrange.span(), (6, 7))
    self.assertEqual(moddedobjnodes[3], objnode3)
    self.assertEqual(moddedobjnodes[3].positionrange.span(), (10, 11))

  def test_insert_overwrite5 (self):

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
    moddedobjnode = ObjectNode.insert(PositionRange(5, 6), objnode4, objnode1, InsertionMode.OVERWRITE)
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 4)
    self.assertEqual(moddedobjnodes[0], objnode1)
    self.assertEqual(moddedobjnodes[0].positionrange.span(), (2, 3))
    self.assertEqual(moddedobjnodes[1], objnode4)
    self.assertEqual(moddedobjnodes[1].positionrange.span(), (5, 6))
    self.assertEqual(moddedobjnodes[2], objnode2)
    self.assertEqual(moddedobjnodes[2].positionrange.span(), (7, 7))
    self.assertEqual(moddedobjnodes[3], objnode3)
    self.assertEqual(moddedobjnodes[3].positionrange.span(), (10, 11))

  def test_insert_overwrite6 (self):

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
    moddedobjnode = ObjectNode.insert(PositionRange(6, 7), objnode4, objnode1, InsertionMode.OVERWRITE)
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(moddedobjnodes[0], objnode1)
    self.assertEqual(moddedobjnodes[0].positionrange.span(), (2, 3))
    self.assertEqual(moddedobjnodes[1], objnode4)
    self.assertEqual(moddedobjnodes[1].positionrange.span(), (6, 7))
    self.assertEqual(moddedobjnodes[2], objnode3)
    self.assertEqual(moddedobjnodes[2].positionrange.span(), (10, 11))

  def test_insert_overwrite7 (self):

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
    moddedobjnode = ObjectNode.insert(PositionRange(7, 8), objnode4, objnode1, InsertionMode.OVERWRITE)
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 4)
    self.assertEqual(moddedobjnodes[0], objnode1)
    self.assertEqual(moddedobjnodes[0].positionrange.span(), (2, 3))
    self.assertEqual(moddedobjnodes[1], objnode2)
    self.assertEqual(moddedobjnodes[1].positionrange.span(), (6, 6))
    self.assertEqual(moddedobjnodes[2], objnode4)
    self.assertEqual(moddedobjnodes[2].positionrange.span(), (7, 8))
    self.assertEqual(moddedobjnodes[3], objnode3)
    self.assertEqual(moddedobjnodes[3].positionrange.span(), (10, 11))

  def test_insert_overwrite8 (self):

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
    moddedobjnode = ObjectNode.insert(PositionRange(8, 9), objnode4, objnode1, InsertionMode.OVERWRITE)
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 4)
    self.assertEqual(moddedobjnodes[0], objnode1)
    self.assertEqual(moddedobjnodes[0].positionrange.span(), (2, 3))
    self.assertEqual(moddedobjnodes[1], objnode2)
    self.assertEqual(moddedobjnodes[1].positionrange.span(), (6, 7))
    self.assertEqual(moddedobjnodes[2], objnode4)
    self.assertEqual(moddedobjnodes[2].positionrange.span(), (8, 9))
    self.assertEqual(moddedobjnodes[3], objnode3)
    self.assertEqual(moddedobjnodes[3].positionrange.span(), (10, 11))

  def test_insert_overwrite9 (self):

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
    moddedobjnode = ObjectNode.insert(PositionRange(9, 10), objnode4, objnode1, InsertionMode.OVERWRITE)
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 4)
    self.assertEqual(moddedobjnodes[0], objnode1)
    self.assertEqual(moddedobjnodes[0].positionrange.span(), (2, 3))
    self.assertEqual(moddedobjnodes[1], objnode2)
    self.assertEqual(moddedobjnodes[1].positionrange.span(), (6, 7))
    self.assertEqual(moddedobjnodes[2], objnode4)
    self.assertEqual(moddedobjnodes[2].positionrange.span(), (9, 10))
    self.assertEqual(moddedobjnodes[3], objnode3)
    self.assertEqual(moddedobjnodes[3].positionrange.span(), (11, 11))

  def test_insert_overwrite10 (self):

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
    moddedobjnode = ObjectNode.insert(PositionRange(10, 11), objnode4, objnode1, InsertionMode.OVERWRITE)
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(moddedobjnodes[0], objnode1)
    self.assertEqual(moddedobjnodes[0].positionrange.span(), (2, 3))
    self.assertEqual(moddedobjnodes[1], objnode2)
    self.assertEqual(moddedobjnodes[1].positionrange.span(), (6, 7))
    self.assertEqual(moddedobjnodes[2], objnode4)
    self.assertEqual(moddedobjnodes[2].positionrange.span(), (10, 11))

  def test_insert_overwrite11 (self):

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
    moddedobjnode = ObjectNode.insert(PositionRange(11, 12), objnode4, objnode1, InsertionMode.OVERWRITE)
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 4)
    self.assertEqual(moddedobjnodes[0], objnode1)
    self.assertEqual(moddedobjnodes[0].positionrange.span(), (2, 3))
    self.assertEqual(moddedobjnodes[1], objnode2)
    self.assertEqual(moddedobjnodes[1].positionrange.span(), (6, 7))
    self.assertEqual(moddedobjnodes[2], objnode3)
    self.assertEqual(moddedobjnodes[2].positionrange.span(), (10, 10))
    self.assertEqual(moddedobjnodes[3], objnode4)
    self.assertEqual(moddedobjnodes[3].positionrange.span(), (11, 12))

  def test_insert_overwrite12 (self):

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
    moddedobjnode = ObjectNode.insert(PositionRange(12, 13), objnode4, objnode1, InsertionMode.OVERWRITE)
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 4)
    self.assertEqual(moddedobjnodes[0], objnode1)
    self.assertEqual(moddedobjnodes[0].positionrange.span(), (2, 3))
    self.assertEqual(moddedobjnodes[1], objnode2)
    self.assertEqual(moddedobjnodes[1].positionrange.span(), (6, 7))
    self.assertEqual(moddedobjnodes[2], objnode3)
    self.assertEqual(moddedobjnodes[2].positionrange.span(), (10, 11))
    self.assertEqual(moddedobjnodes[3], objnode4)
    self.assertEqual(moddedobjnodes[3].positionrange.span(), (12, 13))
