import unittest
from src.the_shortest_safe_route import *


class TestBFSShortMinesPath(unittest.TestCase):
    def test_normal_case(self):
        grid = [
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        self.assertEqual(the_shortest_safe_route(grid), 12)

    def test_shortest_path_is_not_from_first_node(self):
        grid = [
            [1, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
        ]
        self.assertEqual(the_shortest_safe_route(grid), 6)

    def test_empty_input(self):
        grid = [[]]
        self.assertEqual(the_shortest_safe_route(grid), -1)