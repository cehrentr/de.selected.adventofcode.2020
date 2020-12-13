from copy import deepcopy
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)


class AdventOfCodePuzzleDay11:
    """
    --- Day 11: Seating System ---
    Your plane lands with plenty of time to spare. The final leg of your journey is a
    ferry that goes directly to the tropical island where you can finally start your
    vacation. As you reach the waiting area to board the ferry, you realize you're so
    early, nobody else has even arrived yet!

    By modeling the process people use to choose (or abandon) their seat in the waiting
    area, you're pretty sure you can predict the best place to sit. You make a quick map
    of the seat layout (your puzzle input).

    The seat layout fits neatly on a grid. Each position is either floor (.), an empty
    seat (L), or an occupied seat (#). For example, the initial seat layout might look
    like this:

    L.LL.LL.LL
    LLLLLLL.LL
    L.L.L..L..
    LLLL.LL.LL
    L.LL.LL.LL
    L.LLLLL.LL
    ..L.L.....
    LLLLLLLLLL
    L.LLLLLL.L
    L.LLLLL.LL

    Now, you just need to model the people who will be arriving shortly. Fortunately,
    people are entirely predictable and always follow a simple set of rules. All decisions
    are based on the number of occupied seats adjacent to a given seat (one of the eight
    positions immediately up, down, left, right, or diagonal from the seat). The following
    rules are applied to every seat simultaneously:

    - If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes
      occupied.
    - If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the
      seat becomes empty.
    - Otherwise, the seat's state does not change.

    Floor (.) never changes; seats don't move, and nobody sits on the floor.

    After one round of these rules, every seat in the example layout becomes occupied:

    #.##.##.##
    #######.##
    #.#.#..#..
    ####.##.##
    #.##.##.##
    #.#####.##
    ..#.#.....
    ##########
    #.######.#
    #.#####.##

    After a second round, the seats with four or more occupied adjacent seats become empty again:

    #.LL.L#.##
    #LLLLLL.L#
    L.L.L..L..
    #LLL.LL.L#
    #.LL.LL.LL
    #.LLLL#.##
    ..L.L.....
    #LLLLLLLL#
    #.LLLLLL.L
    #.#LLLL.##

    This process continues for three more rounds:

    #.##.L#.##
    #L###LL.L#
    L.#.#..#..
    #L##.##.L#
    #.##.LL.LL
    #.###L#.##
    ..#.#.....
    #L######L#
    #.LL###L.L
    #.#L###.##
    #.#L.L#.##
    #LLL#LL.L#
    L.L.L..#..
    #LLL.##.L#
    #.LL.LL.LL
    #.LL#L#.##
    ..L.L.....
    #L#LLLL#L#
    #.LLLLLL.L
    #.#L#L#.##
    #.#L.L#.##
    #LLL#LL.L#
    L.#.L..#..
    #L##.##.L#
    #.#L.LL.LL
    #.#L#L#.##
    ..L.L.....
    #L#L##L#L#
    #.LLLLLL.L
    #.#L#L#.##

    At this point, something interesting happens: the chaos stabilizes and further
    applications of these rules cause no seats to change state! Once people stop
    moving around, you count 37 occupied seats.

    Simulate your seating area by applying the seating rules repeatedly until no seats
    change state. How many seats end up occupied?
    """

    EMPTY = "L"
    TAKEN = "#"
    FLOOR = "."

    # (row_step, seat_step)
    DIRECTIONS = {
        "upper_left": (-1, -1),
        "upper": (-1, 0),
        "upper_right": (-1, 1),
        "left": (0, -1),
        "right": (0, 1),
        "lower_left": (1, -1),
        "lower": (1, 0),
        "lower_right": (1, 1)
    }

    def __init__(self, puzzle_input: list):
        self.seat_layout = [row.replace("\n", "") for row in puzzle_input]
        self.number_of_rows = len(self.seat_layout)
        self.number_of_seats = len(self.seat_layout[0])

    def solve_puzzle_1(self) -> int:
        optimized_layout = deepcopy(self.seat_layout)
        testing_layout = deepcopy(optimized_layout)

        while True:
            for row_idx, row in enumerate(optimized_layout):
                new_row = ""

                for seat_idx, seat in enumerate(row):
                    surrounding_seats = self.__get_surrounding_seats(optimized_layout, row_idx, seat_idx)

                    if seat == self.EMPTY and surrounding_seats.count(self.TAKEN) == 0:
                        new_row += self.TAKEN
                    elif seat == self.TAKEN and surrounding_seats.count(self.TAKEN) >= 4:
                        new_row += self.EMPTY
                    else:
                        new_row += seat

                testing_layout[row_idx] = new_row

            if optimized_layout == testing_layout:
                result = sum([row.count("#") for row in optimized_layout])
                break
            else:
                optimized_layout = deepcopy(testing_layout)

        return result

    def solve_puzzle_2(self) -> int:
        optimized_layout = deepcopy(self.seat_layout)
        testing_layout = deepcopy(optimized_layout)

        while True:
            for row_idx, row in enumerate(optimized_layout):
                # print(optimized_layout)

                new_row = ""

                for seat_idx, seat in enumerate(row):
                    visible_occupied_seats = self.__get_visible_occupied_seats(optimized_layout, row_idx, seat_idx)
                    # print(visible_occupied_seats)

                    if seat == self.EMPTY and visible_occupied_seats.count(self.TAKEN) == 0:
                        new_row += self.TAKEN
                    elif seat == self.TAKEN and visible_occupied_seats.count(self.TAKEN) >= 5:
                        new_row += self.EMPTY
                    else:
                        new_row += seat

                # print(f"old_row={row}; new_row={new_row}")

                testing_layout[row_idx] = new_row

            if optimized_layout == testing_layout:
                # print(f"optimized_layout={optimized_layout}; testing_layout={testing_layout}")
                result = sum([row.count("#") for row in optimized_layout])
                break
            else:
                optimized_layout = deepcopy(testing_layout)

        return result

    # def _test_example(self):
    #     visible_occupied_seats = self.__get_visible_occupied_seats(self.seat_layout, 1, 1)
    #     print(visible_occupied_seats)

    def __get_surrounding_seats(self, layout: list, row_idx: int, seat_idx: int) -> list:
        seats = []

        for direction in self.DIRECTIONS:
            row_step, seat_step = self.DIRECTIONS[direction][0], self.DIRECTIONS[direction][1]

            if (
                (row_idx + row_step) < 0 or
                (row_idx + row_step) >= self.number_of_rows or
                (seat_idx + seat_step) < 0 or
                (seat_idx + seat_step) >= self.number_of_seats
            ):
                seats.append(self.EMPTY)
            else:
                seats.append(layout[row_idx + row_step][seat_idx + seat_step])

        return seats

    def __get_visible_occupied_seats(self, layout: list, row_idx: int, seat_idx: int) -> list:
        seats = []

        for direction in self.DIRECTIONS:
            row_step, seat_step = self.DIRECTIONS[direction][0], self.DIRECTIONS[direction][1]
            sum_row_steps, sum_seat_steps = row_step, seat_step

            while row_idx >= 0 or seat_idx >= 0:

                if (
                    (row_idx + sum_row_steps) < 0 or
                    (row_idx + sum_row_steps) >= self.number_of_rows or
                    (seat_idx + sum_seat_steps) < 0 or
                    (seat_idx + sum_seat_steps) >= self.number_of_seats
                ):
                    seats.append(self.EMPTY)
                    break

                seat = layout[row_idx + sum_row_steps][seat_idx + sum_seat_steps]

                if seat in [self.TAKEN, self.EMPTY]:
                    seats.append(seat)
                    break

                sum_row_steps += row_step
                sum_seat_steps += seat_step

        return seats
