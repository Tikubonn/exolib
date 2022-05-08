
from unittest import TestCase
from exolib import Node

class ExampleNode (Node):

  pass

class TestNode (TestCase):

  def test_forwards (self):
    node1 = ExampleNode()
    node2 = ExampleNode()
    node3 = ExampleNode()
    node1.link_forward(node2)
    node2.link_forward(node3)
    nodeiter = iter(node1.forwards())
    self.assertEqual(next(nodeiter), node1)
    self.assertEqual(next(nodeiter), node2)
    self.assertEqual(next(nodeiter), node3)
    with self.assertRaises(StopIteration):
      next(nodeiter)

  def test_backwards (self):
    node1 = ExampleNode()
    node2 = ExampleNode()
    node3 = ExampleNode()
    node1.link_forward(node2)
    node2.link_forward(node3)
    nodeiter = iter(node3.backwards())
    self.assertEqual(next(nodeiter), node3)
    self.assertEqual(next(nodeiter), node2)
    self.assertEqual(next(nodeiter), node1)
    with self.assertRaises(StopIteration):
      next(nodeiter)

  def test_independent (self):
    node1 = ExampleNode()
    node2 = ExampleNode()
    node3 = ExampleNode()
    node1.link_forward(node2)
    node2.link_forward(node3)
    node1.independent() 
    self.assertEqual(node1.backward, None)
    self.assertEqual(node1.forward, None)
    self.assertEqual(node2.backward, None)

    #test iterate independent node to forward.

    nodeiterforward = iter(node1.forwards())
    self.assertEqual(next(nodeiterforward), node1)
    with self.assertRaises(StopIteration):
      next(nodeiterforward)

    #test iterate modified node to forward.

    nodeiterforward = iter(node2.forwards())
    self.assertEqual(next(nodeiterforward), node2)
    self.assertEqual(next(nodeiterforward), node3)
    with self.assertRaises(StopIteration):
      next(nodeiterforward)

    #test iterate independent node to backward.

    nodeiterbackward = iter(node1.backwards())
    self.assertEqual(next(nodeiterbackward), node1)
    with self.assertRaises(StopIteration):
      next(nodeiterbackward)

    #test iterate modified node to backward.

    nodeiterbackward = iter(node3.backwards())
    self.assertEqual(next(nodeiterbackward), node3)
    self.assertEqual(next(nodeiterbackward), node2)
    with self.assertRaises(StopIteration):
      next(nodeiterbackward)

  def test_independent2 (self):
    node1 = ExampleNode()
    node2 = ExampleNode()
    node3 = ExampleNode()
    node1.link_forward(node2)
    node2.link_forward(node3)
    node2.independent() 
    self.assertEqual(node1.forward, node3)
    self.assertEqual(node2.backward, None)
    self.assertEqual(node2.forward, None)
    self.assertEqual(node3.backward, node1)

    #test iterate independent node to forward.

    nodeiterforward = iter(node2.forwards())
    self.assertEqual(next(nodeiterforward), node2)
    with self.assertRaises(StopIteration):
      next(nodeiterforward)

    #test iterate modified node to forward.

    nodeiterforward = iter(node1.forwards())
    self.assertEqual(next(nodeiterforward), node1)
    self.assertEqual(next(nodeiterforward), node3)
    with self.assertRaises(StopIteration):
      next(nodeiterforward)

    #test iterate independent node to backward.

    nodeiterbackward = iter(node2.backwards())
    self.assertEqual(next(nodeiterbackward), node2)
    with self.assertRaises(StopIteration):
      next(nodeiterbackward)

    #test iterate modified node to backward.

    nodeiterbackward = iter(node3.backwards())
    self.assertEqual(next(nodeiterbackward), node3)
    self.assertEqual(next(nodeiterbackward), node1)
    with self.assertRaises(StopIteration):
      next(nodeiterbackward)

  def test_independent3 (self):
    node1 = ExampleNode()
    node2 = ExampleNode()
    node3 = ExampleNode()
    node1.link_forward(node2)
    node2.link_forward(node3)
    node3.independent() 
    self.assertEqual(node2.forward, None)
    self.assertEqual(node3.backward, None)
    self.assertEqual(node3.forward, None)

    #test iterate independent node to forward.

    nodeiterforward = iter(node3.forwards())
    self.assertEqual(next(nodeiterforward), node3)
    with self.assertRaises(StopIteration):
      next(nodeiterforward)

    #test iterate modified node to forward.

    nodeiterforward = iter(node1.forwards())
    self.assertEqual(next(nodeiterforward), node1)
    self.assertEqual(next(nodeiterforward), node2)
    with self.assertRaises(StopIteration):
      next(nodeiterforward)

    #test iterate independent node to backward.

    nodeiterbackward = iter(node3.backwards())
    self.assertEqual(next(nodeiterbackward), node3)
    with self.assertRaises(StopIteration):
      next(nodeiterbackward)

    #test iterate modified node to backward.

    nodeiterbackward = iter(node2.backwards())
    self.assertEqual(next(nodeiterbackward), node2)
    self.assertEqual(next(nodeiterbackward), node1)
    with self.assertRaises(StopIteration):
      next(nodeiterbackward)

  def test_first (self):
    node1 = ExampleNode()
    node2 = ExampleNode()
    node3 = ExampleNode()
    node1.link_forward(node2)
    node2.link_forward(node3)
    self.assertEqual(node1.first(), node1)
    self.assertEqual(node2.first(), node1)
    self.assertEqual(node3.first(), node1)

  def test_last (self):
    node1 = ExampleNode()
    node2 = ExampleNode()
    node3 = ExampleNode()
    node1.link_forward(node2)
    node2.link_forward(node3)
    self.assertEqual(node1.last(), node3)
    self.assertEqual(node2.last(), node3)
    self.assertEqual(node3.last(), node3)

  def test_link_forward (self):
    node1 = ExampleNode()
    node2 = ExampleNode()
    node3 = ExampleNode()
    node1.link_forward(node2)
    node2.link_forward(node3)
    node4 = ExampleNode()
    node1.link_forward(node4)

    #test iterate modified node to forward.

    nodeiterforward = iter(node1.forwards())
    self.assertEqual(next(nodeiterforward), node1)
    self.assertEqual(next(nodeiterforward), node4)
    self.assertEqual(next(nodeiterforward), node2)
    self.assertEqual(next(nodeiterforward), node3)
    with self.assertRaises(StopIteration):
      next(nodeiterforward)

    #test iterate modified node to backward.

    nodeiterbackward = iter(node3.backwards())
    self.assertEqual(next(nodeiterbackward), node3)
    self.assertEqual(next(nodeiterbackward), node2)
    self.assertEqual(next(nodeiterbackward), node4)
    self.assertEqual(next(nodeiterbackward), node1)
    with self.assertRaises(StopIteration):
      next(nodeiterbackward)

  def test_link_forward2 (self):
    node1 = ExampleNode()
    node2 = ExampleNode()
    node3 = ExampleNode()
    node1.link_forward(node2)
    node2.link_forward(node3)
    node4 = ExampleNode()
    node2.link_forward(node4)

    #test iterate modified node to forward.

    nodeiterforward = iter(node1.forwards())
    self.assertEqual(next(nodeiterforward), node1)
    self.assertEqual(next(nodeiterforward), node2)
    self.assertEqual(next(nodeiterforward), node4)
    self.assertEqual(next(nodeiterforward), node3)
    with self.assertRaises(StopIteration):
      next(nodeiterforward)

    #test iterate modified node to backward.

    nodeiterbackward = iter(node3.backwards())
    self.assertEqual(next(nodeiterbackward), node3)
    self.assertEqual(next(nodeiterbackward), node4)
    self.assertEqual(next(nodeiterbackward), node2)
    self.assertEqual(next(nodeiterbackward), node1)
    with self.assertRaises(StopIteration):
      next(nodeiterbackward)

  def test_link_forward3 (self):
    node1 = ExampleNode()
    node2 = ExampleNode()
    node3 = ExampleNode()
    node1.link_forward(node2)
    node2.link_forward(node3)
    node4 = ExampleNode()
    node3.link_forward(node4)

    #test iterate modified node to forward.

    nodeiterforward = iter(node1.forwards())
    self.assertEqual(next(nodeiterforward), node1)
    self.assertEqual(next(nodeiterforward), node2)
    self.assertEqual(next(nodeiterforward), node3)
    self.assertEqual(next(nodeiterforward), node4)
    with self.assertRaises(StopIteration):
      next(nodeiterforward)

    #test iterate modified node to backward.

    nodeiterbackward = iter(node4.backwards())
    self.assertEqual(next(nodeiterbackward), node4)
    self.assertEqual(next(nodeiterbackward), node3)
    self.assertEqual(next(nodeiterbackward), node2)
    self.assertEqual(next(nodeiterbackward), node1)
    with self.assertRaises(StopIteration):
      next(nodeiterbackward)

  def test_link_backward (self):
    node1 = ExampleNode()
    node2 = ExampleNode()
    node3 = ExampleNode()
    node1.link_forward(node2)
    node2.link_forward(node3)
    node4 = ExampleNode()
    node1.link_backward(node4)

    #test iterate modified node to forward.

    nodeiterforward = iter(node4.forwards())
    self.assertEqual(next(nodeiterforward), node4)
    self.assertEqual(next(nodeiterforward), node1)
    self.assertEqual(next(nodeiterforward), node2)
    self.assertEqual(next(nodeiterforward), node3)
    with self.assertRaises(StopIteration):
      next(nodeiterforward)

    #test iterate modified node to backward.

    nodeiterbackward = iter(node3.backwards())
    self.assertEqual(next(nodeiterbackward), node3)
    self.assertEqual(next(nodeiterbackward), node2)
    self.assertEqual(next(nodeiterbackward), node1)
    self.assertEqual(next(nodeiterbackward), node4)
    with self.assertRaises(StopIteration):
      next(nodeiterbackward)

  def test_link_backward2 (self):
    node1 = ExampleNode()
    node2 = ExampleNode()
    node3 = ExampleNode()
    node1.link_forward(node2)
    node2.link_forward(node3)
    node4 = ExampleNode()
    node2.link_backward(node4)

    #test iterate modified node to forward.

    nodeiterforward = iter(node1.forwards())
    self.assertEqual(next(nodeiterforward), node1)
    self.assertEqual(next(nodeiterforward), node4)
    self.assertEqual(next(nodeiterforward), node2)
    self.assertEqual(next(nodeiterforward), node3)
    with self.assertRaises(StopIteration):
      next(nodeiterforward)

    #test iterate modified node to backward.

    nodeiterbackward = iter(node3.backwards())
    self.assertEqual(next(nodeiterbackward), node3)
    self.assertEqual(next(nodeiterbackward), node2)
    self.assertEqual(next(nodeiterbackward), node4)
    self.assertEqual(next(nodeiterbackward), node1)
    with self.assertRaises(StopIteration):
      next(nodeiterbackward)

  def test_link_backward3 (self):
    node1 = ExampleNode()
    node2 = ExampleNode()
    node3 = ExampleNode()
    node1.link_forward(node2)
    node2.link_forward(node3)
    node4 = ExampleNode()
    node3.link_backward(node4)

    #test iterate modified node to forward.

    nodeiterforward = iter(node1.forwards())
    self.assertEqual(next(nodeiterforward), node1)
    self.assertEqual(next(nodeiterforward), node2)
    self.assertEqual(next(nodeiterforward), node4)
    self.assertEqual(next(nodeiterforward), node3)
    with self.assertRaises(StopIteration):
      next(nodeiterforward)

    #test iterate modified node to backward.

    nodeiterbackward = iter(node3.backwards())
    self.assertEqual(next(nodeiterbackward), node3)
    self.assertEqual(next(nodeiterbackward), node4)
    self.assertEqual(next(nodeiterbackward), node2)
    self.assertEqual(next(nodeiterbackward), node1)
    with self.assertRaises(StopIteration):
      next(nodeiterbackward)

  def test_move_forward (self):
    node1 = ExampleNode()
    node2 = ExampleNode()
    node3 = ExampleNode()
    node1.link_forward(node2)
    node2.link_forward(node3)
    node1.move_forward()

    #test iterate modified node to forward.

    nodeiterforward = iter(node2.forwards())
    self.assertEqual(next(nodeiterforward), node2)
    self.assertEqual(next(nodeiterforward), node1)
    self.assertEqual(next(nodeiterforward), node3)
    with self.assertRaises(StopIteration):
      next(nodeiterforward)

    #test iterate modified node to backward.

    nodeiterbackward = iter(node3.backwards())
    self.assertEqual(next(nodeiterbackward), node3)
    self.assertEqual(next(nodeiterbackward), node1)
    self.assertEqual(next(nodeiterbackward), node2)
    with self.assertRaises(StopIteration):
      next(nodeiterbackward)

  def test_move_forward2 (self):
    node1 = ExampleNode()
    node2 = ExampleNode()
    node3 = ExampleNode()
    node1.link_forward(node2)
    node2.link_forward(node3)
    node2.move_forward()

    #test iterate modified node to forward.

    nodeiterforward = iter(node1.forwards())
    self.assertEqual(next(nodeiterforward), node1)
    self.assertEqual(next(nodeiterforward), node3)
    self.assertEqual(next(nodeiterforward), node2)
    with self.assertRaises(StopIteration):
      next(nodeiterforward)

    #test iterate modified node to backward.

    nodeiterbackward = iter(node2.backwards())
    self.assertEqual(next(nodeiterbackward), node2)
    self.assertEqual(next(nodeiterbackward), node3)
    self.assertEqual(next(nodeiterbackward), node1)
    with self.assertRaises(StopIteration):
      next(nodeiterbackward)

  def test_move_forward3 (self):
    node1 = ExampleNode()
    node2 = ExampleNode()
    node3 = ExampleNode()
    node1.link_forward(node2)
    node2.link_forward(node3)
    node3.move_forward()

    #test iterate modified node to forward.

    nodeiterforward = iter(node1.forwards())
    self.assertEqual(next(nodeiterforward), node1)
    self.assertEqual(next(nodeiterforward), node2)
    self.assertEqual(next(nodeiterforward), node3)
    with self.assertRaises(StopIteration):
      next(nodeiterforward)

    #test iterate modified node to backward.

    nodeiterbackward = iter(node3.backwards())
    self.assertEqual(next(nodeiterbackward), node3)
    self.assertEqual(next(nodeiterbackward), node2)
    self.assertEqual(next(nodeiterbackward), node1)
    with self.assertRaises(StopIteration):
      next(nodeiterbackward)

  def test_move_backward (self):
    node1 = ExampleNode()
    node2 = ExampleNode()
    node3 = ExampleNode()
    node1.link_forward(node2)
    node2.link_forward(node3)
    node1.move_backward()

    #test iterate modified node to forward.

    nodeiterforward = iter(node1.forwards())
    self.assertEqual(next(nodeiterforward), node1)
    self.assertEqual(next(nodeiterforward), node2)
    self.assertEqual(next(nodeiterforward), node3)
    with self.assertRaises(StopIteration):
      next(nodeiterforward)

    #test iterate modified node to backward.

    nodeiterbackward = iter(node3.backwards())
    self.assertEqual(next(nodeiterbackward), node3)
    self.assertEqual(next(nodeiterbackward), node2)
    self.assertEqual(next(nodeiterbackward), node1)
    with self.assertRaises(StopIteration):
      next(nodeiterbackward)

  def test_move_backward2 (self):
    node1 = ExampleNode()
    node2 = ExampleNode()
    node3 = ExampleNode()
    node1.link_forward(node2)
    node2.link_forward(node3)
    node2.move_backward()

    #test iterate modified node to forward.

    nodeiterforward = iter(node2.forwards())
    self.assertEqual(next(nodeiterforward), node2)
    self.assertEqual(next(nodeiterforward), node1)
    self.assertEqual(next(nodeiterforward), node3)
    with self.assertRaises(StopIteration):
      next(nodeiterforward)

    #test iterate modified node to backward.

    nodeiterbackward = iter(node3.backwards())
    self.assertEqual(next(nodeiterbackward), node3)
    self.assertEqual(next(nodeiterbackward), node1)
    self.assertEqual(next(nodeiterbackward), node2)
    with self.assertRaises(StopIteration):
      next(nodeiterbackward)

  def test_move_backward3 (self):
    node1 = ExampleNode()
    node2 = ExampleNode()
    node3 = ExampleNode()
    node1.link_forward(node2)
    node2.link_forward(node3)
    node3.move_backward()

    #test iterate modified node to forward.

    nodeiterforward = iter(node1.forwards())
    self.assertEqual(next(nodeiterforward), node1)
    self.assertEqual(next(nodeiterforward), node3)
    self.assertEqual(next(nodeiterforward), node2)
    with self.assertRaises(StopIteration):
      next(nodeiterforward)

    #test iterate modified node to backward.

    nodeiterbackward = iter(node2.backwards())
    self.assertEqual(next(nodeiterbackward), node2)
    self.assertEqual(next(nodeiterbackward), node3)
    self.assertEqual(next(nodeiterbackward), node1)
    with self.assertRaises(StopIteration):
      next(nodeiterbackward)
