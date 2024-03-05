import unittest
from find_unsorted_subarray.labs.find_max_count_of_hamsters import max_hamsters
class TestMaxHamsters(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(max_hamsters(7, 3, [[1, 2], [2, 2], [3, 1]]), 2)

    def test_example_2(self):
        self.assertEqual(max_hamsters(19, 4, [[5, 0], [2, 2], [1, 4], [5, 1]]), 3)

    def test_example_3(self):
        self.assertEqual(max_hamsters(1000, 9, [[10000, 1], [1000, 1], [3000, 1], [500, 1], [300, 1], [700, 1], [600, 1], [400, 2], [50, 80]]), 3)

    def test_example_4(self):
        self.assertEqual(max_hamsters(2, 2, [[1, 50000], [1, 60000]]), 1)

    def test_no_hamsters(self):
        self.assertRaises(ValueError,max_hamsters,10,0,[])

    def test_one_hamster(self):
        self.assertEqual(max_hamsters(5, 1, [[3, 1]]), 1)

    def test_all_greedy_hamsters(self):
        self.assertEqual(max_hamsters(10, 3, [[2, 3], [3, 3], [4, 3]]), 1)

    def test_no_food(self):
        self.assertEqual(max_hamsters(0, 5, [[3, 1], [4, 2], [5, 3]]), 0)

    def test_empty_hamsters(self):
        sum_of_eat = 10
        count_of_hamsters = 0
        hamsters = []
        self.assertRaises(ValueError, max_hamsters, sum_of_eat, count_of_hamsters, hamsters)

    def test_large_food_supply(self):
        sum_of_eat = 100
        count_of_hamsters = 5
        hamsters = [[10, 5], [20, 3], [15, 2], [25, 4], [30, 1]]
        self.assertEqual(max_hamsters(sum_of_eat, count_of_hamsters, hamsters), 3)

    def test_small_food_supply(self):
        sum_of_eat = 5
        count_of_hamsters = 3
        hamsters = [[3, 2], [2, 3], [4, 1]]
        self.assertEqual(max_hamsters(sum_of_eat, count_of_hamsters, hamsters), 1)

    def test_all_greedy_hamsters(self):
        sum_of_eat = 20
        count_of_hamsters = 4
        hamsters = [[5, 2], [5, 3], [5, 4], [5, 5]]
        self.assertEqual(max_hamsters(sum_of_eat, count_of_hamsters, hamsters), 2)

    def test_all_equal_greediness(self):
        sum_of_eat = 15
        count_of_hamsters = 3
        hamsters = [[5, 2], [5, 2], [5, 2]]
        self.assertEqual(max_hamsters(sum_of_eat, count_of_hamsters, hamsters), 2)


if __name__ == "__main__":
    unittest.main()