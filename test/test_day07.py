import unittest
from src.advent_of_code_2020.day_07.solution import AdventOfCodePuzzleDay07


class TestAdventOfCodePuzzleDay07(unittest.TestCase):
    
    def test_solution_day_07_puzzle_1_example(self):
        with open("./testdata/input_day07_example.txt", "r") as fil:
            input_data = fil.read()

        solution = AdventOfCodePuzzleDay07(input_data).solve_puzzle_1()
        self.assertEqual(4, solution)

    def test_solution_day_07_puzzle_1(self):
        with open("./testdata/input_day07.txt", "r") as fil:
            input_data = fil.read()

        solution = AdventOfCodePuzzleDay07(input_data).solve_puzzle_1()
        self.assertEqual(248, solution)

    def test_solution_day_07_puzzle_2_example1(self):
        with open("./testdata/input_day07_example.txt", "r") as fil:
            input_data = fil.read()

        solution = AdventOfCodePuzzleDay07(input_data).solve_puzzle_2()
        self.assertEqual(32, solution)

    def test_solution_day_07_puzzle_2_example2(self):
        with open("./testdata/input_day07_example2.txt", "r") as fil:
            input_data = fil.read()

        solution = AdventOfCodePuzzleDay07(input_data).solve_puzzle_2()
        self.assertEqual(126, solution)

    def test_solution_day_07_puzzle_2(self):
        with open("./testdata/input_day07.txt", "r") as fil:
            input_data = fil.read()

        solution = AdventOfCodePuzzleDay07(input_data).solve_puzzle_2()
        self.assertEqual(57281, solution)


if __name__ == '__main__':
    unittest.main(verbosity=True)
