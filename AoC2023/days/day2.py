from itertools import product
from math import prod

from AoC2023.base.day import Day


class Day2(Day):
    tests = ["""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""]
    part1_answers = [8]
    part2_answers = [2286]

    def parse(self):
        data = {}
        for line in self.file:
            game, draws = line.split(':')
            _, game_num = game.strip().split(" ")
            rounds = draws.split(";")
            game_rounds = []
            for r in rounds:
                sets = r.split(",")
                rdict = {}
                for s in sets:
                    num, col = s.strip().split(" ")
                    rdict[col.strip()] = int(num.strip())
                game_rounds.append(rdict)
            data[int(game_num)] = game_rounds
        return data

    def part1(self):
        valid_rounds = []
        for r, draws in self.parse().items():
            seen = {"red": 0, "green": 0, "blue": 0}
            for draw in draws:
                for col, count in draw.items():
                    seen[col] = max(seen[col], count)
            if seen["red"] <= 12 and seen["green"] <= 13 and seen["blue"] <= 14:
                valid_rounds.append(r)
        return sum(valid_rounds)

    def part2(self):
        powers = []
        for r, draws in self.parse().items():
            seen = {"red": 0, "green": 0, "blue": 0}
            for draw in draws:
                for col, count in draw.items():
                    seen[col] = max(seen[col], count)
            powers.append(prod(seen.values()))
        return sum(powers)


