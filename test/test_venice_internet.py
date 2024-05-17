import unittest
from src.venice_internet import find_min_len_cable_in_the_island


class VehicleInternetTest(unittest.TestCase):
    def test_empty_graph(self):
        find_min_len_cable_in_the_island("./resources/islands_empty.csv", "./resources/islands_empty.out")
        with open("./resources/islands_empty.out", 'r') as file:
            first_line = file.readline()
        self.assertEqual(first_line, "Graph is empty")

    def test_normal_graph(self):
        find_min_len_cable_in_the_island("./resources/islands.csv", "./resources/islands.out")
        with open("./resources/islands.out", 'r') as file:
            first_line = file.readline()
            numbers = first_line.split()
        self.assertEqual(int(numbers[0]), 30)