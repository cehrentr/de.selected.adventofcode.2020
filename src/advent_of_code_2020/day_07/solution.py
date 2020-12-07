import re
import json
import collections


class AdventOfCodePuzzleDay07:
    """
    --- Day 7: Handy Haversacks ---
    You land at the regional airport in time for your next flight. In fact, it
    looks like you'll even have time to grab some food: all flights are currently
    delayed due to issues in luggage processing.

    Due to recent aviation regulations, many rules (your puzzle input) are being
    enforced about bags and their contents; bags must be color-coded and must
    contain specific quantities of other color-coded bags. Apparently, nobody
    responsible for these regulations considered how long they would take to
    enforce!

    For example, consider the following rules:

    light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    bright white bags contain 1 shiny gold bag.
    muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    faded blue bags contain no other bags.
    dotted black bags contain no other bags.

    These rules specify the required contents for 9 bag types. In this example,
    every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded
    blue and 6 dotted black), and so on.

    You have a shiny gold bag. If you wanted to carry it in at least one other bag,
    how many different bag colors would be valid for the outermost bag? (In other
    words: how many colors can, eventually, contain at least one shiny gold bag?)

    In the above rules, the following options would be available to you:

    A bright white bag, which can hold your shiny gold bag directly.
    A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
    A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
    A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.

    So, in this example, the number of bag colors that can eventually contain at least
    one shiny gold bag is 4.

    How many bag colors can eventually contain at least one shiny gold bag? (The list
    of rules is quite long; make sure you get all of it.)
    """

    """
    light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    bright white bags contain 1 shiny gold bag.
    muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    faded blue bags contain no other bags.
    dotted black bags contain no other bags.
    """

    BAGS_PATTERN = re.compile('^([^ ]+ [^ ]+) bags contain (.*)..$')
    BAG_PATTERN = re.compile(r'(\d+) ([^ ]+ [^ ]+)')
    OUR_BAG = "shiny gold"

    def __init__(self, puzzle_input: str):
        self.rules = {}

        for line in puzzle_input.splitlines():
            match = self.BAGS_PATTERN.match(line)
            self.rules[match[1]] = [(int(n), item) for n, item in self.BAG_PATTERN.findall(match[2])]

    def solve_puzzle_1(self) -> int:
        result = 0
        for item in self.rules:
            result += 1 if self.__contains_our_bag(item) else 0

        return result

    def solve_puzzle_2(self) -> int:
        return self.__get_number_of_bags(self.OUR_BAG) - 1

    def __contains_our_bag(self, bag: str) -> bool:
        result = False
        if self.OUR_BAG in [item[1] for item in self.rules[bag]]:
            result = True
        else:
            for item in self.rules[bag]:
                result |= self.__contains_our_bag(item[1])

        return result

    def __get_number_of_bags(self, bag: str) -> int:
        if not self.rules[bag]:
            return 1
        else:
            sum_bags = 0
            recurse_result = 0
            for item in self.rules[bag]:
                bag_quantity = int(item[0])
                recurse_result += bag_quantity * self.__get_number_of_bags(item[1])
            sum_bags += 1 + recurse_result

            return sum_bags
