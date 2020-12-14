import unittest
from src.day_14.solution import AdventOfCodePuzzleDay14


class TestAdventOfCodePuzzleDay14(unittest.TestCase):

    def test_solution_day_14_puzzle_1_example(self):
        input_data = [
            "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
            "mem[8] = 11",
            "mem[7] = 101",
            "mem[8] = 0"
        ]

        solution = AdventOfCodePuzzleDay14(input_data).solve_puzzle_1()
        self.assertEqual(165, solution)

    def test_solution_day_14_puzzle_1(self):
        with open("./testdata/input_day14.txt", "r") as fil:
            input_data = fil.readlines()

        solution = AdventOfCodePuzzleDay14(input_data).solve_puzzle_1()
        self.assertEqual(4886706177792, solution)

    def test_solution_day_14_puzzle_2_example(self):
        input_data = [
            "mask = 000000000000000000000000000000X1001X",
            "mem[42] = 100",
            "mask = 00000000000000000000000000000000X0XX",
            "mem[26] = 1"
        ]

        solution = AdventOfCodePuzzleDay14(input_data).solve_puzzle_2()
        self.assertEqual(208, solution)

    def test_solution_day_14_puzzle_2(self):
        with open("./testdata/input_day14.txt", "r") as fil:
            input_data = fil.readlines()

        solution = AdventOfCodePuzzleDay14(input_data).solve_puzzle_2()
        self.assertEqual(3348493585827, solution)


if __name__ == '__main__':
    unittest.main(verbosity=True)
