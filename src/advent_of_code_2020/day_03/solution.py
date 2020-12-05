class AdventOfCodePuzzleDay03:
    """
    --- Day 3: Toboggan Trajectory ---
    With the toboggan login problems resolved, you set off toward the airport.
    While travel by toboggan might be easy, it's certainly not safe: there's
    very minimal steering and the area is covered in trees. You'll need to see
    which angles will take you near the fewest trees.

    Due to the local geology, trees in this area only grow on exact integer
    coordinates in a grid. You make a map (your puzzle input) of the open
    squares (.) and trees (#) you can see. For example:

    ..##.......
    #...#...#..
    .#....#..#.
    ..#.#...#.#
    .#...##..#.
    ..#.##.....
    .#.#.#....#
    .#........#
    #.##...#...
    #...##....#
    .#..#...#.#

    These aren't the only trees, though; due to something you read about once
    involving arboreal genetics and biome stability, the same pattern repeats
    to the right many times:

    ..##.........##.........##.........##.........##.........##.......  --->
    #...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
    .#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
    ..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
    .#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
    ..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
    .#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
    .#........#.#........#.#........#.#........#.#........#.#........#
    #.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
    #...##....##...##....##...##....##...##....##...##....##...##....#
    .#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

    You start on the open square (.) in the top-left corner and need to reach
    the bottom (below the bottom-most row on your map).

    The toboggan can only follow a few specific slopes (you opted for a cheaper
    model that prefers rational numbers); start by counting all the trees you would
    encounter for the slope right 3, down 1:

    From your starting position at the top-left, check the position that is right
    3 and down 1. Then, check the position that is right 3 and down 1 from there,
    and so on until you go past the bottom of the map.

    The locations you'd check in the above example are marked here with O where
    there was an open square and X where there was a tree:

    ..##.........##.........##.........##.........##.........##.......  --->
    #..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
    .#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
    ..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
    .#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
    ..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
    .#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
    .#........#.#........X.#........#.#........#.#........#.#........#
    #.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
    #...##....##...##....##...#X....##...##....##...##....##...##....#
    .#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

    In this example, traversing the map using this slope would cause you to
    encounter 7 trees.

    Starting at the top-left corner of your map and following a slope of right
    3 and down 1, how many trees would you encounter?
    """

    TREE = "#"

    def __init__(self, puzzle_input: list):
        self.map = puzzle_input
        self.map_width = len(puzzle_input[0])

    def solve_puzzle_1(self, x_step: int, y_step: int) -> int:
        return self.__solve(x_step=x_step, y_step=y_step)

    def solve_puzzle_2(self, slopes: list) -> int:
        product = 1

        for slope in slopes:
            solution = self.__solve(x_step=slope["right"], y_step=slope["down"])
            product *= solution

        return product

    def __solve(self, x_step: int, y_step: int):
        x, y = 0, 0
        result = 0

        while y < (len(self.map) - 1):
            x += x_step
            y += y_step

            if x > len(self.map[y][x]):
                x -= self.map_width

            if self.map[y][x] == self.TREE:
                result += 1

        return result
