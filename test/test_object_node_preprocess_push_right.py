
from exolib import ObjectNode, InsertionError, PositionRange
from unittest import TestCase 

class TestObjectNodePreprocessPushRight (TestCase):

  def test_preprocess_push_right (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_push_right(PositionRange(1, 2))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (3, 4))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (7, 8))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (11, 12))

  def test_preprocess_push_right2 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_push_right(PositionRange(2, 3))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (4, 5))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (8, 9))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (12, 13))

  def test_preprocess_push_right3 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_push_right(PositionRange(3, 4))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (5, 6))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (9, 10))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (13, 14))

  def test_preprocess_push_right4 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_push_right(PositionRange(4, 5))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (6, 7))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (10, 11))

  def test_preprocess_push_right5 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_push_right(PositionRange(5, 6))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (7, 8))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (11, 12))

  def test_preprocess_push_right6 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_push_right(PositionRange(6, 7))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (8, 9))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (12, 13))

  def test_preprocess_push_right7 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_push_right(PositionRange(7, 8))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (9, 10))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (13, 14))

  def test_preprocess_push_right8 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_push_right(PositionRange(8, 9))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (6, 7))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (10, 11))

  def test_preprocess_push_right9 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_push_right(PositionRange(9, 10))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (6, 7))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (11, 12))

  def test_preprocess_push_right10 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_push_right(PositionRange(10, 11))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (6, 7))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (12, 13))

  def test_preprocess_push_right11 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_push_right(PositionRange(11, 12))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (6, 7))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (13, 14))

  def test_preprocess_push_right12 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_push_right(PositionRange(12, 13))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (6, 7))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (10, 11))
