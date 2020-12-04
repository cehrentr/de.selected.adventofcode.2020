import unittest
from src.advent_of_code_2020.day_01.solution import AdventOfCodePuzzleDay01


class TestAdventOfCodePuzzleDay01(unittest.TestCase):

    def setUp(self) -> None:
        self.input_day01 = []
        with open("./testdata/input_day01.txt", "r") as fil:
            self.input_day01 = [int(line.strip()) for line in fil.readlines()]

    def test_solution_day_01_puzzle_1_example(self):
        solution = AdventOfCodePuzzleDay01([1721, 979, 366, 299, 675, 1456]).solve_puzzle_1()
        self.assertEqual(solution, 514579)

    def test_solution_day_01_puzzle_1(self):
        solution = AdventOfCodePuzzleDay01(self.input_day01).solve_puzzle_1()
        self.assertEqual(solution, 776064)

    def test_solution_day_01_puzzle_2_example(self):
        solution = AdventOfCodePuzzleDay01([1721, 979, 366, 299, 675, 1456]).solve_puzzle_2()
        self.assertEqual(solution, 241861950)

    def test_solution_day_01_puzzle_2(self):
        solution = AdventOfCodePuzzleDay01(self.input_day01).solve_puzzle_2()
        self.assertEqual(solution, 6964490)


if __name__ == '__main__':
    unittest.main(verbosity=True)
