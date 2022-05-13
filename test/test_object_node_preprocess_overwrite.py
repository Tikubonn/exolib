
from exolib import ObjectNode, InsertionError, PositionRange
from unittest import TestCase 

class TestObjectNodePreprocessOverwrite (TestCase):

  def test_preprocess_overwrite (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_overwrite(PositionRange(1, 2))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (3, 3))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (6, 7))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (10, 11))

  def test_preprocess_overwrite2 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_overwrite(PositionRange(2, 3))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 2)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (6, 7))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (10, 11))

  def test_preprocess_overwrite3 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_overwrite(PositionRange(3, 4))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 2))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (6, 7))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (10, 11))

  def test_preprocess_overwrite4 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_overwrite(PositionRange(4, 5))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (6, 7))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (10, 11))

  def test_preprocess_overwrite5 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_overwrite(PositionRange(5, 6))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (7, 7))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (10, 11))

  def test_preprocess_overwrite6 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_overwrite(PositionRange(6, 7))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 2)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (10, 11))

  def test_preprocess_overwrite7 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_overwrite(PositionRange(7, 8))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (6, 6))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (10, 11))

  def test_preprocess_overwrite8 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_overwrite(PositionRange(8, 9))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (6, 7))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (10, 11))

  def test_preprocess_overwrite9 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_overwrite(PositionRange(9, 10))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (6, 7))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (11, 11))

  def test_preprocess_overwrite10 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_overwrite(PositionRange(10, 11))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 2)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (6, 7))

  def test_preprocess_overwrite11 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_overwrite(PositionRange(11, 12))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (6, 7))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (10, 10))

  def test_preprocess_overwrite12 (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    moddedobjnode = objnode1._preprocess_overwrite(PositionRange(12, 13))
    moddedobjnodes = list(moddedobjnode)
    self.assertEqual(len(moddedobjnodes), 3)
    self.assertEqual(tuple(moddedobjnodes[0].positionrange), (2, 3))
    self.assertEqual(tuple(moddedobjnodes[1].positionrange), (6, 7))
    self.assertEqual(tuple(moddedobjnodes[2].positionrange), (10, 11))
