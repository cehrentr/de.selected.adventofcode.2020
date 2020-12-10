import unittest
from src.day_10.solution import AdventOfCodePuzzleDay10


class TestAdventOfCodePuzzleDay10(unittest.TestCase):

    def test_solution_day_10_puzzle_1_example_1(self):
        input_data = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]

        solution = AdventOfCodePuzzleDay10(input_data).solve_puzzle_1()
        self.assertEqual(35, solution)

    def test_solution_day_10_puzzle_1_example_2(self):
        input_data = [
            28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19,
            38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3
        ]

        solution = AdventOfCodePuzzleDay10(input_data).solve_puzzle_1()
        self.assertEqual(220, solution)

    def test_solution_day_10_puzzle_1(self):
        with open("./testdata/input_day10.txt", "r") as fil:
            input_data = [int(item) for item in fil.readlines()]

        solution = AdventOfCodePuzzleDay10(input_data).solve_puzzle_1()
        self.assertEqual(2775, solution)

    def test_solution_day_10_puzzle_2_example_1(self):
        input_data = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]

        solution = AdventOfCodePuzzleDay10(input_data).solve_puzzle_2()
        self.assertEqual(8, solution)

    def test_solution_day_10_puzzle_2_example_2(self):
        input_data = [
            28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19,
            38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3
        ]

        solution = AdventOfCodePuzzleDay10(input_data).solve_puzzle_2()
        self.assertEqual(19208, solution)

    def test_solution_day_10_puzzle_2(self):
        with open("./testdata/input_day10.txt", "r") as fil:
            input_data = [int(item) for item in fil.readlines()]

        solution = AdventOfCodePuzzleDay10(input_data).solve_puzzle_2()
        self.assertEqual(518344341716992, solution)


if __name__ == '__main__':
    unittest.main(verbosity=True)
