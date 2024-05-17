import unittest

from src.avl_priority_queue import AVLTree


class TestAVLTree(unittest.TestCase):

    def setUp(self):
        self.tree = AVLTree()

    def test_insert_single_node(self):
        self.tree.insert(10, 1)
        self.assertEqual(self.tree.root.value, 10)
        self.assertEqual(self.tree.root.priority, 1)
        self.assertEqual(self.tree.root.height, 1)

    def test_insert_multiple_nodes(self):
        self.tree.insert(20, 5)
        self.tree.insert(15, 3)
        self.tree.insert(25, 7)

        self.assertEqual(self.tree.root.value, 20)
        self.assertEqual(self.tree.root.left.value, 25)
        self.assertEqual(self.tree.root.right.value, 15)

    def test_dequeue_node(self):
        self.tree.insert(20, 5)
        self.tree.insert(15, 3)
        self.tree.insert(25, 7)
        self.tree.insert(10, 2)

        node = self.tree.dequeue()
        self.assertEqual(node, (25, 7))

        node = self.tree.dequeue()
        self.assertEqual(self.tree.root.left, None)

if __name__ == "__main__":
    unittest.main()
