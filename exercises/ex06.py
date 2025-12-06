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
        token_positions = lines = []
        # Not optimized read but we do not care for this exercise
        with open(self._input_filepath, 'r') as f:
            lines = f.readlines()
        
        last_line = lines[-1]
        # once we have the last line, we have the alignment, and we can
        # paddle the rest
        current_position = 0
        token_positions = [position for position, character in enumerate(last_line[1:]) if character in ['+', '*']]
        token_positions.append(len(last_line))

        # Pre-allocate
        self._VALUES = [ [] for i in range(len(token_positions)) ]
        
        for values in lines[0:-1]:
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
