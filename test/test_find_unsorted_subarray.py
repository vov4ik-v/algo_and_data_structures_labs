import unittest
from find_unsorted_subarray.lab1.find_unsorted_subarray import find_unsorted_subarray


class TestFindUnsortedSubarray(unittest.TestCase):
    def test_sorted_array(self):
        self.assertEqual(find_unsorted_subarray([1, 2, 3, 4, 5]), (-1, -1))

    def test_reversed_sort_array(self):
        self.assertEqual(find_unsorted_subarray([5, 4, 3, 2, 1]), (0, 4))

    def test_single_element_array(self):
        self.assertEqual(find_unsorted_subarray([1]), (-1, -1))

    def test_unsorted(self):
        self.assertEqual(find_unsorted_subarray([1, 2, 3, 4, 5,-1]), (0,5))


if __name__ == "__main__":
    unittest.main()
