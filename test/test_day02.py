import unittest
from src.advent_of_code_2020.day_02.solution import AdventOfCodePuzzleDay02


class TestAdventOfCodePuzzleDay02(unittest.TestCase):

    def setUp(self) -> None:
        with open("./testdata/input_day02.txt", "r") as fil:
            self.input_data = [line.strip() for line in fil.readlines()]

    def test_solution_day_02_puzzle_1_example(self):
        solution = AdventOfCodePuzzleDay02(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]).solve_puzzle_1()
        self.assertEqual(solution, 2)

    def test_solution_day_02_puzzle_1(self):
        solution = AdventOfCodePuzzleDay02(self.input_data).solve_puzzle_1()
        self.assertEqual(solution, 454)

    def test_solution_day_02_puzzle_2_example(self):
        solution = AdventOfCodePuzzleDay02(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]).solve_puzzle_2()
        self.assertEqual(solution, 1)

    def test_solution_day_02_puzzle_2(self):
        solution = AdventOfCodePuzzleDay02(self.input_data).solve_puzzle_2()
        self.assertEqual(solution, 649)


if __name__ == '__main__':
    unittest.main(verbosity=True)
