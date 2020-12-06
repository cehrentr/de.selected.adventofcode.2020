class AdventOfCodePuzzleDay05:
    """
    --- Day 5: Binary Boarding ---
    You board your plane only to discover a new problem: you dropped your
    boarding pass! You aren't sure which seat is yours, and all of the
    flight attendants are busy with the flood of people that suddenly made
    it through passport control.

    You write a quick program to use your phone's camera to scan all of the
    nearby boarding passes (your puzzle input); perhaps you can find your seat
    through process of elimination.

    Instead of zones or groups, this airline uses binary space partitioning
    to seat people. A seat might be specified like FBFBBFFRLR, where F means
    "front", B means "back", L means "left", and R means "right".

    The first 7 characters will either be F or B; these specify exactly one
    of the 128 rows on the plane (numbered 0 through 127). Each letter tells
    you which half of a region the given seat is in. Start with the whole list
    of rows; the first letter indicates whether the seat is in the front
    (0 through 63) or the back (64 through 127). The next letter indicates
    which half of that region the seat is in, and so on until you're left
    with exactly one row.

    For example, consider just the first seven characters of FBFBBFFRLR:

    Start by considering the whole range, rows 0 through 127.
    F means to take the lower half, keeping rows 0 through 63.
    B means to take the upper half, keeping rows 32 through 63.
    F means to take the lower half, keeping rows 32 through 47.
    B means to take the upper half, keeping rows 40 through 47.
    B keeps rows 44 through 47.
    F keeps rows 44 through 45.
    The final F keeps the lower of the two, row 44.

    The last three characters will be either L or R; these specify exactly one of
    the 8 columns of seats on the plane (numbered 0 through 7). The same process
    as above proceeds again, this time with only three steps. L means to keep the
    lower half, while R means to keep the upper half.

    For example, consider just the last 3 characters of FBFBBFFRLR:

    Start by considering the whole range, columns 0 through 7.
    R means to take the upper half, keeping columns 4 through 7.
    L means to take the lower half, keeping columns 4 through 5.
    The final R keeps the upper of the two, column 5.

    So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

    Every seat also has a unique seat ID: multiply the row by 8, then add the column.
    In this example, the seat has ID 44 * 8 + 5 = 357.

    Here are some other boarding passes:

    BFFFBBFRRR: row 70, column 7, seat ID 567.
    FFFBBBFRRR: row 14, column 7, seat ID 119.
    BBFFBBFRLL: row 102, column 4, seat ID 820.
    As a sanity check, look through your list of boarding passes. What is the
    highest seat ID on a boarding pass?
    """

    MULTIPLIER = 8
    NUMBER_OF_ROWS = list(range(128))
    NUMBER_OF_COLUMNS = list(range(8))

    def __init__(self, puzzle_input: list):
        self.boarding_passes = puzzle_input

    def solve_puzzle_1(self) -> int:
        highest_seat_id = 0

        for b_pass in self.boarding_passes:
            row = self.__get_id(items=self.NUMBER_OF_ROWS, directions=b_pass[:7])
            col = self.__get_id(items=self.NUMBER_OF_COLUMNS, directions=b_pass[-3:])
            seat_id = row * self.MULTIPLIER + col
            highest_seat_id = seat_id if seat_id > highest_seat_id else highest_seat_id

        return highest_seat_id

    def solve_puzzle_1a(self) -> int:
        highest_seat_id = 0

        for line in self.boarding_passes:
            line = line.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0')
            highest_seat_id = max(highest_seat_id, int(line, 2))

        return highest_seat_id

    def solve_puzzle_2(self) -> int:
        all_seat_ids = [
            row * self.MULTIPLIER + col for row in self.NUMBER_OF_ROWS for col in self.NUMBER_OF_COLUMNS
        ]

        taken_seat_ids = []
        for b_pass in self.boarding_passes:
            row = self.__get_id(items=self.NUMBER_OF_ROWS, directions=b_pass[:7])
            col = self.__get_id(items=self.NUMBER_OF_COLUMNS, directions=b_pass[-3:])
            taken_seat_ids.append(row * self.MULTIPLIER + col)

        seat_id = self.__find_seat_id(all_seat_ids=all_seat_ids, taken_seat_ids=taken_seat_ids)

        return seat_id

    def solve_puzzle_2a(self) -> int:
        possible = set(range(1024))

        for line in self.boarding_passes:
            line = line.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0')
            possible.discard(int(line, 2))

        for candidate in possible:
            if candidate - 1 not in possible and candidate + 1 not in possible:
                return candidate
        else:
            raise NotImplementedError('unreachable')

    def __get_id(self, items: list, directions: str):
        for direct in directions:
            items = self.__split_list(direction=direct, split_list=items)

        return items[0]

    @staticmethod
    def __split_list(direction: str, split_list: list) -> list:
        return split_list[:len(split_list)//2] if direction in ["F", "L"] else split_list[len(split_list)//2:]

    @staticmethod
    def __find_seat_id(all_seat_ids: list, taken_seat_ids: list) -> int:
        taken_seat_ids = sorted(taken_seat_ids)
        free_seat_ids = set(all_seat_ids) - set(taken_seat_ids)

        for free_seat_id in free_seat_ids:
            try:
                seat_id_before_taken = (free_seat_id - 1) in taken_seat_ids
                seat_id_after_taken = (free_seat_id + 1) in taken_seat_ids

                if seat_id_before_taken and seat_id_after_taken:
                    return free_seat_id
            except ValueError:
                continue

        return -1
