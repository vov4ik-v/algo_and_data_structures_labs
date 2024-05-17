from src.ijones import *
import unittest


class TestIndianaJones(unittest.TestCase):
    def test_first_case(self):
        row_size, col_size, sneaky_way = read_input_matrix("./resources/ijones_1_case.in")
        result = indiana_jones_traversal(sneaky_way, rows=row_size, cols=col_size)
        out_put = read_output("./resources/ijones_1_case.out")
        self.assertEqual(result, out_put)

    def test_second_case(self):
        row_size, col_size, sneaky_way = read_input_matrix("./resources/ijones_2_case.in")
        result = indiana_jones_traversal(sneaky_way, rows=row_size, cols=col_size)
        out_put = read_output("./resources/ijones_2_case.out")
        self.assertEqual(result, out_put)


    def test_third_case(self):
        row_size, col_size, sneaky_way = read_input_matrix("./resources/ijones_3_case.in")
        result = indiana_jones_traversal(sneaky_way, rows=row_size, cols=col_size)
        out_put = read_output("./resources/ijones_3_case.out")
        self.assertEqual(result, out_put)

if __name__ == "__main__":
    unittest.main()