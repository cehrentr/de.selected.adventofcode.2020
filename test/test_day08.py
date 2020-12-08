import unittest
from src.day_08.solution import AdventOfCodePuzzleDay08


class TestAdventOfCodePuzzleDay08(unittest.TestCase):
    
    def test_solution_day_08_puzzle_1_example(self):
        with open("./testdata/input_day08_example.txt", "r") as fil:
            input_data = fil.readlines()

        solution = AdventOfCodePuzzleDay08(input_data).solve_puzzle_1()
        self.assertEqual(5, solution)

    def test_solution_day_08_puzzle_1(self):
        with open("./testdata/input_day08.txt", "r") as fil:
            input_data = fil.readlines()

        solution = AdventOfCodePuzzleDay08(input_data).solve_puzzle_1()
        self.assertEqual(1528, solution)

    def test_solution_day_08_puzzle_2_example(self):
        with open("./testdata/input_day08_example.txt", "r") as fil:
            input_data = fil.readlines()

        solution = AdventOfCodePuzzleDay08(input_data).solve_puzzle_2()
        self.assertEqual(8, solution)

    def test_solution_day_08_puzzle_2(self):
        with open("./testdata/input_day08.txt", "r") as fil:
            input_data = fil.readlines()

        solution = AdventOfCodePuzzleDay08(input_data).solve_puzzle_2()
        self.assertEqual(640, solution)


if __name__ == '__main__':
    unittest.main(verbosity=True)
