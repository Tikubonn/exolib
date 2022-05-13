
from exolib import ObjectNode, InsertionError, PositionRange
from unittest import TestCase 

class TestObjectNodePreprocessPushLeft (TestCase):

  def test_preprocess_push_left (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    with self.assertRaises(InsertionError):
      objnode1._preprocess_push_left(PositionRange(1, 2))

  def test_preprocess_push_left2 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    with self.assertRaises(InsertionError):
      objnode1._preprocess_push_left(PositionRange(2, 3))

  def test_preprocess_push_left3 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_push_left(PositionRange(3, 4))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (1, 2))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (6, 7))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (10, 11))

  def test_preprocess_push_left4 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_push_left(PositionRange(4, 5))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (6, 7))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (10, 11))

  def test_preprocess_push_left5 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    with self.assertRaises(InsertionError):
      objnode1._preprocess_push_left(PositionRange(5, 6))

  def test_preprocess_push_left6 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    with self.assertRaises(InsertionError):
      objnode1._preprocess_push_left(PositionRange(6, 7))

  def test_preprocess_push_left7 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_push_left(PositionRange(7, 8))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (1, 2))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (5, 6))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (10, 11))

  def test_preprocess_push_left8 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_push_left(PositionRange(8, 9))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (6, 7))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (10, 11))

  def test_preprocess_push_left9 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    with self.assertRaises(InsertionError):
      objnode1._preprocess_push_left(PositionRange(9, 10))

  def test_preprocess_push_left10 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    with self.assertRaises(InsertionError):
      objnode1._preprocess_push_left(PositionRange(10, 11))

  def test_preprocess_push_left11 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    self.assertEqual(objnode1._can_preprocess_push_left(PositionRange(11, 12)), True)
    moddedobjnode = objnode1._preprocess_push_left(PositionRange(11, 12))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (1, 2))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (5, 6))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (9, 10))

  def test_preprocess_push_left12 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    self.assertEqual(objnode1._can_preprocess_push_left(PositionRange(12, 13)), True)
    moddedobjnode = objnode1._preprocess_push_left(PositionRange(12, 13))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (6, 7))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (10, 11))
