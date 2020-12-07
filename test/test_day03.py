import unittest
from day_03.solution import AdventOfCodePuzzleDay03


class TestAdventOfCodePuzzleDay03(unittest.TestCase):

    def setUp(self) -> None:
        self.slopes = [
            {"right": 1, "down": 1},
            {"right": 3, "down": 1},
            {"right": 5, "down": 1},
            {"right": 7, "down": 1},
            {"right": 1, "down": 2}
        ]

    def test_solution_day_03_puzzle_1_example(self):
        with open("./testdata/input_day03_example.txt", "r") as fil:
            input_data = [line.strip() for line in fil.readlines()]

        solution = AdventOfCodePuzzleDay03(input_data).solve_puzzle_1(x_step=3, y_step=1)
        self.assertEqual(solution, 7)

    def test_solution_day_03_puzzle_1(self):
        with open("./testdata/input_day03.txt", "r") as fil:
            input_data = [line.strip() for line in fil.readlines()]

        solution = AdventOfCodePuzzleDay03(input_data).solve_puzzle_1(x_step=3, y_step=1)
        self.assertEqual(solution, 181)

    def test_solution_day_03_puzzle_2_example(self):
        with open("./testdata/input_day03_example.txt", "r") as fil:
            input_data = [line.strip() for line in fil.readlines()]

        solution = AdventOfCodePuzzleDay03(input_data).solve_puzzle_2(slopes=self.slopes)
        self.assertEqual(solution, 336)

    def test_solution_day_03_puzzle_2(self):
        with open("./testdata/input_day03.txt", "r") as fil:
            input_data = [line.strip() for line in fil.readlines()]

        solution = AdventOfCodePuzzleDay03(input_data).solve_puzzle_2(slopes=self.slopes)
        self.assertEqual(solution, 1260601650)


if __name__ == '__main__':
    unittest.main(verbosity=True)
