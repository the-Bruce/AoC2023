import string

from AoC2023.base.day import Day


class Day1(Day):
    tests = ["""1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""", """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""]
    part1_answers = [142, None]
    part2_answers = [None, 281]

    def part1(self):
        numbers = []
        for line in self.file:
            filtered = [a for a in line if a in string.digits]
            numbers.append(int(f"{filtered[0]}{filtered[-1]}"))
        return sum(numbers)

    def part2(self):
        spellings = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
                     '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
        numbers = []
        for line in self.file:
            line = line.strip()
            # print("line", line)
            x = line
            first = None
            while len(x) > 0 and first is None:
                for prefix in range(6):
                    if x[:prefix] in spellings:
                        first = spellings[x[:prefix]]
                        break
                x=x[1:]
            x = line
            last = None
            while len(x) > 0 and last is None:
                for prefix in range(7):
                    # print("last", x, prefix, x[-prefix:])
                    if x[-prefix:] in spellings:
                        # print("last found:", x[-prefix:])
                        last = spellings[x[-prefix:]]
                        break
                x=x[:-1]
            numbers.append(int(f"{first}{last}"))
        return sum(numbers)
