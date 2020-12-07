import unittest
from day_05.solution import AdventOfCodePuzzleDay05


class TestAdventOfCodePuzzleDay05(unittest.TestCase):
    
    def test_solution_day_05_puzzle_1_example(self):
        with open("./testdata/input_day05_example.txt", "r") as fil:
            input_data = [line.rstrip() for line in fil.readlines()]

        solution = AdventOfCodePuzzleDay05(input_data).solve_puzzle_1()
        self.assertEqual(solution, 357)

    def test_solution_day_05_puzzle_1(self):
        with open("./testdata/input_day05.txt", "r") as fil:
            input_data = [line.rstrip() for line in fil.readlines()]

        solution = AdventOfCodePuzzleDay05(input_data).solve_puzzle_1()
        self.assertEqual(solution, 906)

    def test_solution_day_05_puzzle_1a_example(self):
        with open("./testdata/input_day05_example.txt", "r") as fil:
            input_data = [line.rstrip() for line in fil.readlines()]

        solution = AdventOfCodePuzzleDay05(input_data).solve_puzzle_1a()
        self.assertEqual(solution, 357)

    def test_solution_day_05_puzzle_2(self):
        with open("./testdata/input_day05.txt", "r") as fil:
            input_data = [line.rstrip() for line in fil.readlines()]

        solution = AdventOfCodePuzzleDay05(input_data).solve_puzzle_2()
        self.assertEqual(solution, 519)

    def test_solution_day_05_puzzle_2a(self):
        with open("./testdata/input_day05.txt", "r") as fil:
            input_data = [line.rstrip() for line in fil.readlines()]

        solution = AdventOfCodePuzzleDay05(input_data).solve_puzzle_2a()
        self.assertEqual(solution, 519)


if __name__ == '__main__':
    unittest.main(verbosity=True)
