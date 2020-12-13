import unittest
from src.day_11.solution import AdventOfCodePuzzleDay11


class TestAdventOfCodePuzzleDay11(unittest.TestCase):

    def test_solution_day_11_puzzle_1_example_1(self):
        with open("./testdata/input_day11_example.txt", "r") as fil:
            input_data = fil.readlines()

        solution = AdventOfCodePuzzleDay11(input_data).solve_puzzle_1()
        self.assertEqual(37, solution)

    def test_solution_day_11_puzzle_1(self):
        with open("./testdata/input_day11.txt", "r") as fil:
            input_data = fil.readlines()

        solution = AdventOfCodePuzzleDay11(input_data).solve_puzzle_1()
        self.assertEqual(2386, solution)

    def test_solution_day_11_puzzle_2_example(self):
        with open("./testdata/input_day11_example.txt", "r") as fil:
            input_data = fil.readlines()

        solution = AdventOfCodePuzzleDay11(input_data).solve_puzzle_2()
        self.assertEqual(26, solution)

    def test_solution_day_11_puzzle_2(self):
        with open("./testdata/input_day11.txt", "r") as fil:
            input_data = fil.readlines()

        solution = AdventOfCodePuzzleDay11(input_data).solve_puzzle_2()
        self.assertEqual(2091, solution)


if __name__ == '__main__':
    unittest.main(verbosity=True)
