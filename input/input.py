class Input:

    def __init__(self, cast = str):
        self.cast = cast

    @property
    def bonus(self):
        return self._read_input("bonus_input.txt")

    @property
    def example(self):
        return self._read_input("example_input.txt")

    @property
    def puzzle(self):
        return self._read_input("puzzle_input.txt")

    def _read_input(self, file):
        return [self.cast(line.rstrip('\n')) if line.rstrip('\n') else None for line in open(file, "r")]