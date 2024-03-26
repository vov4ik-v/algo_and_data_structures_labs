import unittest
from src.game_server import *
from src.avl_priority_queue import AVLTree


class TestGameServerLatency(unittest.TestCase):
    def test_incomplete_connections_list(self):
        find_minimum_latency_from_file("../resources/gamsrv.in", "../resources/gamsrv.out")
        with open('../resources/gamsrv.out', 'r') as file:
            first_line = file.readline()
            numbers = first_line.split()

        self.assertEqual(int(numbers[0]), 100)

    def test_big_num(self):
        find_minimum_latency_from_file("../resources/gamsrv3.in", "../resources/gamsrv3.out")
        with open('../resources/gamsrv3.out', 'r') as file:
            first_line = file.readline()
            numbers = first_line.split()
        self.assertEqual(int(numbers[0]), 1000000000)