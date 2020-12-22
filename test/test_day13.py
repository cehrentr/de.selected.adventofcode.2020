import unittest
from src.day_13.solution import AdventOfCodePuzzleDay13


class TestAdventOfCodePuzzleDay13(unittest.TestCase):

    def test_solution_day_13_puzzle_1_example(self):
        input_data = [
            "939",
            "7,13,x,x,59,x,31,19"
        ]

        solution = AdventOfCodePuzzleDay13(input_data).solve_puzzle_1()
        self.assertEqual(295, solution)

    def test_solution_day_13_puzzle_1(self):
        with open("./testdata/input_day13.txt", "r") as fil:
            input_data = fil.readlines()

        solution = AdventOfCodePuzzleDay13(input_data).solve_puzzle_1()
        self.assertEqual(156, solution)

    def test_solution_day_13_puzzle_2_example_1(self):
        input_data = [
            "939",
            "7,13,x,x,59,x,31,19"
        ]

        solution = AdventOfCodePuzzleDay13(input_data).solve_puzzle_2()
        self.assertEqual(1068781, solution)

    def test_solution_day_13_puzzle_2_example_2(self):
        input_data = [
            "939",
            "17,x,13,19"
        ]

        solution = AdventOfCodePuzzleDay13(input_data).solve_puzzle_2()
        self.assertEqual(3417, solution)

    def test_solution_day_13_puzzle_2_example_3(self):
        input_data = [
            "939",
            "67,7,59,61"
        ]

        solution = AdventOfCodePuzzleDay13(input_data).solve_puzzle_2()
        self.assertEqual(754018, solution)

    def test_solution_day_13_puzzle_2_example_4(self):
        input_data = [
            "939",
            "67,x,7,59,61"
        ]

        solution = AdventOfCodePuzzleDay13(input_data).solve_puzzle_2()
        self.assertEqual(779210, solution)

    def test_solution_day_13_puzzle_2_example_5(self):
        input_data = [
            "939",
            "67,7,x,59,61"
        ]

        solution = AdventOfCodePuzzleDay13(input_data).solve_puzzle_2()
        self.assertEqual(1261476, solution)

    def test_solution_day_13_puzzle_2_example_6(self):
        input_data = [
            "939",
            "1789,37,47,1889"
        ]

        solution = AdventOfCodePuzzleDay13(input_data).solve_puzzle_2()
        self.assertEqual(1202161486, solution)

    def test_solution_day_13_puzzle_2(self):
        with open("./testdata/input_day13.txt", "r") as fil:
            input_data = fil.readlines()

        solution = AdventOfCodePuzzleDay13(input_data).solve_puzzle_2()
        self.assertEqual(3348493585827, solution)


if __name__ == '__main__':
    unittest.main(verbosity=True)
