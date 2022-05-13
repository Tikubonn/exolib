
from exolib import ObjectNode, ObjectParamNode, InsertionMode, InsertionError, PositionRange
from unittest import TestCase 

class TestObjectNode (TestCase):

  def test_list (self):

    # [1 ~ 2] 3 [4 ~ 5] 6 [7 ~ 8]
    
    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    objnodes = list(objnode1)
    self.assertEqual(len(objnodes), 3)
    self.assertEqual(objnodes[0], objnode1)
    self.assertEqual(objnodes[1], objnode2)
    self.assertEqual(objnodes[2], objnode3)

  def test_forwards (self):

    # [1 ~ 2] 3 [4 ~ 5] 6 [7 ~ 8]
    
    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    objnodes = list(objnode1.forwards())
    self.assertEqual(len(objnodes), 3)
    self.assertEqual(objnodes[0], objnode1)
    self.assertEqual(objnodes[1], objnode2)
    self.assertEqual(objnodes[2], objnode3)

  def test_backwards (self):

    # [1 ~ 2] 3 [4 ~ 5] 6 [7 ~ 8]
    
    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    objnodes = list(objnode1.backwards())
    self.assertEqual(len(objnodes), 1)
    self.assertEqual(objnodes[0], objnode1)

  def test_backwards2 (self):

    # [1 ~ 2] 3 [4 ~ 5] 6 [7 ~ 8]
    
    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    objnodes = list(objnode3.backwards())
    self.assertEqual(len(objnodes), 3)
    self.assertEqual(objnodes[0], objnode3)
    self.assertEqual(objnodes[1], objnode2)
    self.assertEqual(objnodes[2], objnode1)

  def test_find_by_position (self):

    # [1 ~ 2] 3 [4 ~ 5] 6 [7 ~ 8]
    
    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(1, 2) #assign to private member.
    objnode2._positionrange = PositionRange(4, 5) #assign to private member.
    objnode3._positionrange = PositionRange(7, 8) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    self.assertEqual(objnode1.find_by_position(1), objnode1)
    self.assertEqual(objnode1.find_by_position(2), objnode1)
    self.assertEqual(objnode1.find_by_position(3), None)
    self.assertEqual(objnode1.find_by_position(4), objnode2)
    self.assertEqual(objnode1.find_by_position(5), objnode2)
    self.assertEqual(objnode1.find_by_position(6), None)
    self.assertEqual(objnode1.find_by_position(7), objnode3)
    self.assertEqual(objnode1.find_by_position(8), objnode3)

  def test_find_by_posrange (self):

    # [1 ~ 2] 3 [4 ~ 5] 6 [7 ~ 8]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(1, 2) #assign to private member.
    objnode2._positionrange = PositionRange(4, 5) #assign to private member.
    objnode3._positionrange = PositionRange(7, 8) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    self.assertEqual(objnode1.find_by_posrange(PositionRange(1, 1)), [ objnode1 ]) #1 ~ 
    self.assertEqual(objnode1.find_by_posrange(PositionRange(1, 3)), [ objnode1 ])
    self.assertEqual(objnode1.find_by_posrange(PositionRange(1, 4)), [ objnode1, objnode2 ])
    self.assertEqual(objnode1.find_by_posrange(PositionRange(1, 6)), [ objnode1, objnode2 ])
    self.assertEqual(objnode1.find_by_posrange(PositionRange(1, 7)), [ objnode1, objnode2, objnode3 ])
    self.assertEqual(objnode1.find_by_posrange(PositionRange(1, 9)), [ objnode1, objnode2, objnode3 ])
    self.assertEqual(objnode1.find_by_posrange(PositionRange(3, 3)), []) #3 ~ 
    self.assertEqual(objnode1.find_by_posrange(PositionRange(3, 4)), [ objnode2 ])
    self.assertEqual(objnode1.find_by_posrange(PositionRange(3, 6)), [ objnode2 ])
    self.assertEqual(objnode1.find_by_posrange(PositionRange(3, 7)), [ objnode2, objnode3 ])
    self.assertEqual(objnode1.find_by_posrange(PositionRange(3, 9)), [ objnode2, objnode3 ])
    self.assertEqual(objnode1.find_by_posrange(PositionRange(4, 4)), [ objnode2 ]) #4 ~ 
    self.assertEqual(objnode1.find_by_posrange(PositionRange(4, 6)), [ objnode2 ])
    self.assertEqual(objnode1.find_by_posrange(PositionRange(4, 7)), [ objnode2, objnode3 ])
    self.assertEqual(objnode1.find_by_posrange(PositionRange(4, 9)), [ objnode2, objnode3 ])
    self.assertEqual(objnode1.find_by_posrange(PositionRange(6, 6)), []) #6 ~ 
    self.assertEqual(objnode1.find_by_posrange(PositionRange(6, 7)), [ objnode3 ])
    self.assertEqual(objnode1.find_by_posrange(PositionRange(6, 9)), [ objnode3 ])
    self.assertEqual(objnode1.find_by_posrange(PositionRange(9, 9)), []) #9 ~ 

  def test_backwards_start_by (self):

    # [1 ~ 2] 3 [4 ~ 5] 6 [7 ~ 8]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(1, 2) #assign to private member.
    objnode2._positionrange = PositionRange(4, 5) #assign to private member.
    objnode3._positionrange = PositionRange(7, 8) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    self.assertEqual(objnode1._backwards_start_by(1), [ objnode1 ])
    self.assertEqual(objnode1._backwards_start_by(2), [ objnode1 ])
    self.assertEqual(objnode1._backwards_start_by(3), [ objnode1 ])
    self.assertEqual(objnode1._backwards_start_by(4), [ objnode2, objnode1 ])
    self.assertEqual(objnode1._backwards_start_by(5), [ objnode2, objnode1 ])
    self.assertEqual(objnode1._backwards_start_by(6), [ objnode2, objnode1 ])
    self.assertEqual(objnode1._backwards_start_by(7), [ objnode3, objnode2, objnode1 ])
    self.assertEqual(objnode1._backwards_start_by(8), [ objnode3, objnode2, objnode1 ])
    self.assertEqual(objnode1._backwards_start_by(9), [ objnode3, objnode2, objnode1 ])

  def test_forwards_start_by (self):

    # [1 ~ 2] 3 [4 ~ 5] 6 [7 ~ 8]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(1, 2) #assign to private member.
    objnode2._positionrange = PositionRange(4, 5) #assign to private member.
    objnode3._positionrange = PositionRange(7, 8) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    self.assertEqual(objnode1._forwards_start_by(1), [ objnode1, objnode2, objnode3 ])
    self.assertEqual(objnode1._forwards_start_by(2), [ objnode1, objnode2, objnode3 ])
    self.assertEqual(objnode1._forwards_start_by(3), [ objnode2, objnode3 ])
    self.assertEqual(objnode1._forwards_start_by(4), [ objnode2, objnode3 ])
    self.assertEqual(objnode1._forwards_start_by(5), [ objnode2, objnode3 ])
    self.assertEqual(objnode1._forwards_start_by(6), [ objnode3 ])
    self.assertEqual(objnode1._forwards_start_by(7), [ objnode3 ])
    self.assertEqual(objnode1._forwards_start_by(8), [ objnode3 ])
    self.assertEqual(objnode1._forwards_start_by(9), [])

  def test_positionize_shift_left (self):

    # [1 ~ 2] 3 ~ 4 [5 ~ 6] 7 ~ 8 [9 ~ 10]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(1, 2) #assign to private member.
    objnode2._positionrange = PositionRange(5, 6) #assign to private member.
    objnode3._positionrange = PositionRange(9, 10) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    with self.assertRaises(InsertionError): objnode1._positionize_shift_left(PositionRange(1, 2))
    with self.assertRaises(InsertionError): objnode1._positionize_shift_left(PositionRange(2, 3))
    self.assertEqual(tuple(objnode1._positionize_shift_left(PositionRange(3, 4))), (3, 4))
    self.assertEqual(tuple(objnode1._positionize_shift_left(PositionRange(4, 5))), (3, 4))
    self.assertEqual(tuple(objnode1._positionize_shift_left(PositionRange(5, 6))), (3, 4))
    self.assertEqual(tuple(objnode1._positionize_shift_left(PositionRange(6, 7))), (3, 4))
    self.assertEqual(tuple(objnode1._positionize_shift_left(PositionRange(7, 8))), (7, 8))
    self.assertEqual(tuple(objnode1._positionize_shift_left(PositionRange(8, 9))), (7, 8))
    self.assertEqual(tuple(objnode1._positionize_shift_left(PositionRange(9, 10))), (7, 8))
    self.assertEqual(tuple(objnode1._positionize_shift_left(PositionRange(10, 11))), (7, 8))
    self.assertEqual(tuple(objnode1._positionize_shift_left(PositionRange(11, 12))), (11, 12))

  def test_positionize_shift_right (self):

    # [1 ~ 2] 3 ~ 4 [5 ~ 6] 7 ~ 8 [9 ~ 10]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(1, 2) #assign to private member.
    objnode2._positionrange = PositionRange(5, 6) #assign to private member.
    objnode3._positionrange = PositionRange(9, 10) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    self.assertEqual(tuple(objnode1._positionize_shift_right(PositionRange(1, 2))), (3, 4))
    self.assertEqual(tuple(objnode1._positionize_shift_right(PositionRange(2, 3))), (3, 4))
    self.assertEqual(tuple(objnode1._positionize_shift_right(PositionRange(3, 4))), (3, 4))
    self.assertEqual(tuple(objnode1._positionize_shift_right(PositionRange(4, 5))), (7, 8))
    self.assertEqual(tuple(objnode1._positionize_shift_right(PositionRange(5, 6))), (7, 8))
    self.assertEqual(tuple(objnode1._positionize_shift_right(PositionRange(6, 7))), (7, 8))
    self.assertEqual(tuple(objnode1._positionize_shift_right(PositionRange(7, 8))), (7, 8))
    self.assertEqual(tuple(objnode1._positionize_shift_right(PositionRange(8, 9))), (11, 12))
    self.assertEqual(tuple(objnode1._positionize_shift_right(PositionRange(9, 10))), (11, 12))
    self.assertEqual(tuple(objnode1._positionize_shift_right(PositionRange(10, 11))), (11, 12))
    self.assertEqual(tuple(objnode1._positionize_shift_right(PositionRange(11, 12))), (11, 12))

  def test_can_preprocess_push_left (self):

    # 1 [2 ~ 3] 4 ~ 5 [6 ~ 7] 8 ~ 9 [10 ~ 11]

    objnode1 = ObjectNode()
    objnode2 = ObjectNode()
    objnode3 = ObjectNode()
    objnode1._positionrange = PositionRange(2, 3) #assign to private member.
    objnode2._positionrange = PositionRange(6, 7) #assign to private member.
    objnode3._positionrange = PositionRange(10, 11) #assign to private member.
    objnode1.link_forward(objnode2)
    objnode2.link_forward(objnode3)
    self.assertEqual(objnode1._can_preprocess_push_left(PositionRange(1, 2)), False)
    self.assertEqual(objnode1._can_preprocess_push_left(PositionRange(2, 3)), False)
    self.assertEqual(objnode1._can_preprocess_push_left(PositionRange(3, 4)), True)
    self.assertEqual(objnode1._can_preprocess_push_left(PositionRange(4, 5)), True)
    self.assertEqual(objnode1._can_preprocess_push_left(PositionRange(5, 6)), False)
    self.assertEqual(objnode1._can_preprocess_push_left(PositionRange(6, 7)), False)
    self.assertEqual(objnode1._can_preprocess_push_left(PositionRange(7, 8)), True)
    self.assertEqual(objnode1._can_preprocess_push_left(PositionRange(8, 9)), True)
    self.assertEqual(objnode1._can_preprocess_push_left(PositionRange(9, 10)), False)
    self.assertEqual(objnode1._can_preprocess_push_left(PositionRange(10, 11)), False)
    self.assertEqual(objnode1._can_preprocess_push_left(PositionRange(11, 12)), True)
    self.assertEqual(objnode1._can_preprocess_push_left(PositionRange(12, 13)), True)

  def test_objparam_node (self):
    objnode = ObjectNode()
    objparamnode1 = ObjectParamNode(_name="example")
    objparamnode2 = ObjectParamNode(_name="example")
    objparamnode3 = ObjectParamNode(_name="example")
    objnode.add_objparam(objparamnode1)
    objnode.add_objparam(objparamnode2)
    objnode.add_objparam(objparamnode3)
    objparamnodes = list(objnode.iter_objparam())
    self.assertEqual(len(objparamnodes), 3)
    self.assertEqual(objparamnodes[0], objparamnode1)
    self.assertEqual(objparamnodes[1], objparamnode2)
    self.assertEqual(objparamnodes[2], objparamnode3)
