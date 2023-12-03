import string
from collections import defaultdict
from functools import cache
from math import prod

from AoC2023.base.day import Day


def adjacent_sym(grid, x, y):
    adjacent_syms = set()
    for x_offset in range(-1, 2):
        for y_offset in range(-1, 2):
            if 0 <= (x + x_offset) < len(grid) and 0 <= (y + y_offset) < len(grid[0]):
                v = grid[x + x_offset][y + y_offset]
                if v != "." and v not in string.digits:
                    adjacent_syms.add((v, x + x_offset, y + y_offset))
    return adjacent_syms


def set_pop(s):
    if len(s) == 1:
        return next(iter(s))
    elif len(s) > 1:
        raise NotImplementedError("Edge case I don't think actually happens?")
    else:
        return None


class Day3(Day):
    tests = ["""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""]
    part1_answers = [4361]
    part2_answers = [467835]

    def parse(self):
        parts = []
        grid = []
        for line in self.file:
            grid.append(list(line.strip()))
        for x, line in enumerate(grid):
            number = None
            adj_syms = None
            for y, char in enumerate(line):
                if char in string.digits:
                    if number is None:
                        number = char
                        adj_syms = adjacent_sym(grid, x, y)
                    else:
                        number += char
                        adj_syms |= adjacent_sym(grid, x, y)
                elif number is not None:
                    parts.append((int(number), set_pop(adj_syms)))
                    number = None
                    adj_syms = None
            if number is not None:
                parts.append((int(number), set_pop(adj_syms)))
        return grid, parts

    def part1(self):
        grid, parts = self.parse()
        acc = 0
        for part, syms in parts:
            if syms is not None:
                acc += part
        return acc

    def part2(self):
        grid, parts = self.parse()
        inverted_parts = defaultdict(list)
        for part, syms in parts:
            if syms is not None and syms[0] == "*":
                inverted_parts[syms].append(part)
        acc = 0
        for part_lst in inverted_parts.values():
            if len(part_lst) == 2:
                acc += prod(part_lst)
        return acc
