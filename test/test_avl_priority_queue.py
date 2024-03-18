import unittest
from src.avl_priority_queue import insert_into_queue, delete_from_queue

class TestPriorityQueue(unittest.TestCase):
    def test_insertion(self):
        root = None
        root = insert_into_queue(root, 'root_node 1', 3)
        root = insert_into_queue(root, 'root_node 2', 1)
        root = insert_into_queue(root, 'root_node 3', 5)
        self.assertEqual(root.value, 'root_node 1')
        self.assertEqual(root.left.value, 'root_node 2')
        self.assertEqual(root.right.value, 'root_node 3')

    def test_priority_duplicates(self):
        root = None
        root = insert_into_queue(root, 'root_node 1', 3)
        root = insert_into_queue(root, 'root_node 2', 1)
        root = insert_into_queue(root, 'root_node 3', 5)
        root = insert_into_queue(root, 'root_node 4', 3)  # Duplicate priority
        root = insert_into_queue(root, 'root_node 5', 3)  # Duplicate priority
        self.assertEqual(root.value, 'root_node 1')  # Highest priority
        self.assertEqual(root.right.value, 'root_node 3')
        self.assertEqual(root.left.value, 'root_node 5')  # Among duplicates, inserted in order
        self.assertEqual(root.left.left.value, 'root_node 2')  # Among duplicates, inserted in order
        self.assertEqual(root.left.right.value, 'root_node 4')  # Among duplicates, inserted in order

    def test_empty_tree(self):
        root = None
        root = delete_from_queue(root)
        self.assertEqual(root, None)

if __name__ == '__main__':
    unittest.main()