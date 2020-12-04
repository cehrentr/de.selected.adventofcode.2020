class AdventOfCodePuzzleDay02:
    """
    --- Day 2: Password Philosophy ---
    Your flight departs in a few days from the coastal airport; the easiest way
    down to the coast from here is via toboggan.

    The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day.
    "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

    Their password database seems to be a little corrupted: some of the passwords
    wouldn't have been allowed by the Official Toboggan Corporate Policy that was
    in effect when they were chosen.

    To try to debug the problem, they have created a list (your puzzle input) of
    passwords (according to the corrupted database) and the corporate policy when
    that password was set.

    For example, suppose you have the following list:

    1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc
    Each line gives the password policy and then the password. The password policy
    indicates the lowest and highest number of times a given letter must appear for
    the password to be valid. For example, 1-3 a means that the password must contain
    a at least 1 time and at most 3 times.

    In the above example, 2 passwords are valid. The middle password, cdefg, is not;
    it contains no instances of b, but needs at least 1. The first and third passwords
    are valid: they contain one a or nine c, both within the limits of their respective
    policies.

    How many passwords are valid according to their policies?
    """

    def __init__(self, puzzle_input: list):
        self.passwords = puzzle_input

    def solve_puzzle_1(self) -> int:
        result = 0

        for item in self.passwords:
            # Parse password
            pwd = item.split(":")[1].lstrip()

            # Parse rule set
            rule = item.split(":")[0]
            rule_range_min = int(rule.split(" ")[0].split("-")[0])
            rule_range_max = int(rule.split(" ")[0].split("-")[1])
            rule_char = rule.split(" ")[1]

            if rule_range_min <= pwd.count(rule_char) <= rule_range_max:
                result += 1

        return result

    def solve_puzzle_2(self) -> int:
        result = 0

        for item in self.passwords:
            # Parse password
            pwd = item.split(":")[1].lstrip()

            # Parse rule set
            rule = item.split(":")[0]
            rule_first_idx = int(rule.split(" ")[0].split("-")[0]) - 1
            rule_second_idx = int(rule.split(" ")[0].split("-")[1]) - 1
            rule_char = rule.split(" ")[1]

            # print(pwd)
            # print(type(pwd[rule_first_idx] == rule_char))
            # print(type(bool(pwd[rule_first_idx] == rule_char)))
            # print('###############################')

            if (pwd[rule_first_idx] == rule_char) ^ (pwd[rule_second_idx] == rule_char):
            # if bool(pwd[rule_first_idx] == rule_char) ^ bool(pwd[rule_second_idx] == rule_char):
                result += 1

        return result
