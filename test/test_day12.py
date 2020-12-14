import unittest
from src.day_12.solution import AdventOfCodePuzzleDay12


class TestAdventOfCodePuzzleDay12(unittest.TestCase):

    def test_solution_day_12_puzzle_1_example(self):
        input_data = ["F10", "N3", "F7", "R90", "F11"]

        solution = AdventOfCodePuzzleDay12(input_data).solve_puzzle_1()
        self.assertEqual(25, solution)

    def test_solution_day_12_puzzle_1(self):
        with open("./testdata/input_day12.txt", "r") as fil:
            input_data = fil.readlines()

        solution = AdventOfCodePuzzleDay12(input_data).solve_puzzle_1()
        self.assertEqual(858, solution)

    def test_solution_day_12_puzzle_2_example(self):
        input_data = ["F10", "N3", "F7", "R90", "F11"]

        solution = AdventOfCodePuzzleDay12(input_data).solve_puzzle_2()
        self.assertEqual(286, solution)

    def test_solution_day_12_puzzle_2(self):
        with open("./testdata/input_day12.txt", "r") as fil:
            input_data = fil.readlines()

        solution = AdventOfCodePuzzleDay12(input_data).solve_puzzle_2()
        self.assertEqual(39140, solution)


if __name__ == '__main__':
    unittest.main(verbosity=True)
