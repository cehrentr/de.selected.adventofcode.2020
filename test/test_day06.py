import unittest
from day_06 import AdventOfCodePuzzleDay06


class TestAdventOfCodePuzzleDay06(unittest.TestCase):
    
    def test_solution_day_06_puzzle_1_example(self):
        with open("./testdata/input_day06_example.txt", "r") as fil:
            input_data = fil.read()

        solution = AdventOfCodePuzzleDay06(input_data).solve_puzzle_1()
        self.assertEqual(solution, 11)

    def test_solution_day_06_puzzle_1(self):
        with open("./testdata/input_day06.txt", "r") as fil:
            input_data = fil.read()

        solution = AdventOfCodePuzzleDay06(input_data).solve_puzzle_1()
        self.assertEqual(solution, 6735)

    def test_solution_day_06_puzzle_2_example(self):
        with open("./testdata/input_day06_example.txt", "r") as fil:
            input_data = fil.read()

        solution = AdventOfCodePuzzleDay06(input_data).solve_puzzle_2()
        self.assertEqual(solution, 6)

    def test_solution_day_06_puzzle_2(self):
        with open("./testdata/input_day06.txt", "r") as fil:
            input_data = fil.read()

        solution = AdventOfCodePuzzleDay06(input_data).solve_puzzle_2()
        self.assertEqual(solution, 3221)


if __name__ == '__main__':
    unittest.main(verbosity=True)
