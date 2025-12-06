from solver import Solver
from typing import List
from collections.abc import Callable
from functools import reduce
import operator
import os

class Operations():
    _operation: Callable[[int, int], int]
    _values: List[int]

    def __init__(self, operation: str, values: List[int]):
        if operation == '+': self._operation = operator.add
        elif operation == '*': self._operation = operator.mul
        else: raise Exception("Operator not found")
        self._values = values

    def transform_for_part2(self):
        _transformed_values = []
        while len(self._values) > 0:
            last_ope_digit = reduce((lambda x, y: x * (10 * len(str(y))) + y), filter(lambda x: x > 0, map(lambda x: x % 10, self._values)))
            self._values = map(lambda x: x // 10, self._values)
            self._values = list(filter(lambda x: x > 0, self._values))
            _transformed_values.append(last_ope_digit)
        self._values = _transformed_values

    def compute(self) -> int:
        return reduce((lambda x, y: self._operation(x, y)), self._values)

class Ex06(Solver):
    _VALUES: List[List[int]] = []
    _OPERATIONS: List[str] = []

    def _parse_inputfile_part1(self):
        with open(self._input_filepath, 'r') as f:
            for line in f:
                stripped_line = line.strip()
                if not stripped_line: continue
                parts = stripped_line.split()
                if len(self._VALUES) != len(parts):
                    self._VALUES = [ [] for i in range(len(parts)) ]

                if parts[0] in ['+', '*']:
                    self._OPERATIONS = parts
                    continue

                for i, part in enumerate(parts):
                    if part == '': continue
                    self._VALUES[i].append(int(part))

        return self._VALUES, self._OPERATIONS

    def _parse_inputfile_part2(self):
        # Read the last line first to get the operator positions
        token_positions = []
        with open(self._input_filepath, 'rb') as f:
            try:  # catch OSError in case of a one line file
                f.seek(-2, os.SEEK_END)
                while f.read(1) != b'\n':
                    f.seek(-2, os.SEEK_CUR)
            except OSError:
                f.seek(0)
            last_line = f.readline().decode()[1:]
            # once we have the last line, we have the alignment, and we can
            # paddle the rest
            current_position = 0
            while current_position < len(last_line):
                if last_line[current_position] in ['*', '+']:
                    token_positions.append(current_position)
                current_position += 1
            token_positions.append(len(last_line))

        # Pre-allocate
        self._VALUES = [ [] for i in range(len(token_positions)) ]

        with open(self._input_filepath, 'r') as f:
            values_lists : List[str] = f.readlines()[:-1] # Do not read again the last line
            for values in values_lists:
                previous_token_position = 0
                for i, position in enumerate(token_positions):
                    cpart = values[previous_token_position:position]
                    cpart = cpart.replace(' ', '0') # We are interested in filling blanks by zeroes...
                    self._VALUES[i].append(int(cpart)) # Magic trick: all right zero values are correctly parsed
                    previous_token_position = position + 1

        return self._VALUES, self._OPERATIONS

    def solve_part1(self):
        result = 0
        values, operations = self._parse_inputfile_part1()

        for i in range(len(values)):
            operation = Operations(operations[i], values[i])
            result += operation.compute()

        return result

    def solve_part2(self):
        result = 0
        values, operations = self._parse_inputfile_part2()

        for i in range(len(values)):
            operation = Operations(operations[i], values[i])
            operation.transform_for_part2() 
            result += operation.compute()

        return result
