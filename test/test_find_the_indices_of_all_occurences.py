import unittest

from src.find_the_indices_of_all_occurrences import find_the_indices_of_all_occurrences


class TestPatternSearch(unittest.TestCase):

    def test_find_occurrences_simple(self):
        pattern = "ababaca"
        text = "abccbababacabbb"
        expected = [5]
        self.assertEqual(find_the_indices_of_all_occurrences(pattern, text), expected)

    def test_find_occurrences_no_occurrence(self):
        pattern = "xyz"
        text = "abccbababacabbb"
        expected = []
        self.assertEqual(find_the_indices_of_all_occurrences(pattern, text), expected)
    #
    # def test_find_occurrences_same_character(self):
    #     pattern = "aaa"
    #     text = "aaabaaa"
    #     expected = [1, 4]
    #     self.assertEqual(find_the_indices_of_all_occurrences(pattern, text), expected)

    def test_find_occurrences_long_pattern(self):
        pattern = "abcdeabcdeabcde"
        text = "abcdeabcdeabcdeabcde"
        expected = [0,5]
        self.assertEqual(find_the_indices_of_all_occurrences(pattern, text), expected)