import unittest
from src.day_09.solution import AdventOfCodePuzzleDay09


class TestAdventOfCodePuzzleDay09(unittest.TestCase):

    def setUp(self) -> None:
        self.preamble_length = 25
    
    def test_solution_day_09_puzzle_1_example_1(self):
        input_data = [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 65, 78
        ]

        solution = AdventOfCodePuzzleDay09(input_data).solve_puzzle_1(self.preamble_length)
        self.assertEqual(65, solution)

    def test_solution_day_09_puzzle_1_example_2(self):
        input_data = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]

        solution = AdventOfCodePuzzleDay09(input_data).solve_puzzle_1(5)
        self.assertEqual(127, solution)

    def test_solution_day_09_puzzle_1(self):
        with open("./testdata/input_day09.txt", "r") as fil:
            input_data = [int(item) for item in fil.readlines()]

        solution = AdventOfCodePuzzleDay09(input_data).solve_puzzle_1(self.preamble_length)
        self.assertEqual(177777905, solution)

    def test_solution_day_09_puzzle_2_example(self):
        input_data = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]

        solution = AdventOfCodePuzzleDay09(input_data).solve_puzzle_2(5)
        self.assertEqual(62, solution)

    def test_solution_day_09_puzzle_2(self):
        with open("./testdata/input_day09.txt", "r") as fil:
            input_data = [int(item) for item in fil.readlines()]

        solution = AdventOfCodePuzzleDay09(input_data).solve_puzzle_2(self.preamble_length)
        self.assertEqual(23463012, solution)


if __name__ == '__main__':
    unittest.main(verbosity=True)
