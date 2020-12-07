import unittest
from day_04 import AdventOfCodePuzzleDay04


class TestAdventOfCodePuzzleDay04(unittest.TestCase):
    
    def test_solution_day_04_puzzle_1_example(self):
        with open("./testdata/input_day04_example.txt", "r") as fil:
            input_data = fil.read()

        solution = AdventOfCodePuzzleDay04(input_data).solve_puzzle_1()
        self.assertEqual(solution, 2)

    def test_solution_day_04_puzzle_1(self):
        with open("./testdata/input_day04.txt", "r") as fil:
            input_data = fil.read()

        solution = AdventOfCodePuzzleDay04(input_data).solve_puzzle_1()
        self.assertEqual(solution, 222)

    def test_solution_day_04_puzzle_2_example_valid(self):
        with open("./testdata/input_day04_part2_example_valid.txt", "r") as fil:
            input_data = fil.read()

        solution = AdventOfCodePuzzleDay04(input_data).solve_puzzle_2()
        self.assertEqual(solution, 4)

    def test_solution_day_04_puzzle_2_example_invalid(self):
        with open("./testdata/input_day04_part2_example_invalid.txt", "r") as fil:
            input_data = fil.read()

        solution = AdventOfCodePuzzleDay04(input_data).solve_puzzle_2()
        self.assertEqual(solution, 0)

    def test_solution_day_04_puzzle_2(self):
        with open("./testdata/input_day04.txt", "r") as fil:
            input_data = fil.read()

        solution = AdventOfCodePuzzleDay04(input_data).solve_puzzle_2()
        self.assertEqual(solution, 140)


if __name__ == '__main__':
    unittest.main(verbosity=True)
