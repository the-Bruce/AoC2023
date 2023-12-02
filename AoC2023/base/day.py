from io import StringIO
from pathlib import Path
from typing import IO

root = Path(__file__).parent.parent.parent


class Day:
    tests = []
    part1_answers = []
    part2_answers = []

    def __init__(self):
        self.file_dir = root / "data" / self.__class__.__name__.lower()
        if not self.file_dir.exists():
            self.file_dir.touch()
        self.file: IO | None = None

    def run(self):
        has_failure = [False, False]
        for i, test in enumerate(self.tests):
            print(f"== Test case {i + 1} ==")
            self.file = StringIO(test)
            print("-- Part 1 --")
            if len(self.part1_answers) > i and self.part1_answers[i] is not None:
                try:
                    res = self._run(self.part1)
                    if res == self.part1_answers[i]:
                        print("Passed")
                    else:
                        has_failure[0] = True
                        print("Failed")
                        print(f"Expected\n{self.part1_answers[i]}")
                        print(f"Got\n{res}")
                except NotImplementedError:
                    print('(Skipped)')
            else:
                print('(Skipped)')
            print("-- Part 2 --")
            if len(self.part2_answers) > i and self.part2_answers[i] is not None:
                try:
                    res = self._run(self.part2)
                    if res == self.part2_answers[i]:
                        print("Passed")
                    else:
                        has_failure[1] = True
                        print("Failed")
                        print(f"Expected\n{self.part2_answers[i]}")
                        print(f"Got\n{res}")
                except NotImplementedError:
                    print('(Skipped)')
            else:
                print('(Skipped)')
            print()
        print("Final result")
        with self.file_dir.open('r') as f:
            self.file = f
            print("Part 1")
            try:
                if has_failure[0]:
                    print('(Skipped)')
                else:
                    print(self._run(self.part1))
            except NotImplementedError:
                print('(Skipped)')
            print()
            print("Part 2")
            try:
                if has_failure[1]:
                    print('(Skipped)')
                else:
                    print(self._run(self.part2))
            except NotImplementedError:
                print('(Skipped)')

    def setup(self):
        pass

    def _run(self, part):
        self.file.seek(0)
        self.setup()
        return part()

    def part1(self):
        raise NotImplementedError()

    def part2(self):
        raise NotImplementedError()
