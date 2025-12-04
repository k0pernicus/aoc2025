from solver import Solver
import logger
from enum import Enum
from copy import deepcopy

CASE_EMPTY = '.'
CASE_ROLL_ACCESS = 'x'
CASE_ROLL = '@'

class Ex04(Solver):
    # Cached parsed input
    _LINES = []

    def _parse_inputfile(self):
        if len(self._LINES) > 0: return self._LINES
        with open(self._input_filepath, 'r') as f:
            for line in f:
                stripped_line = line.strip()
                if not stripped_line: continue
                self._LINES.append(list(stripped_line))
        return self._LINES

    def solve_part1(self):
        result = 0
        lines = self._parse_inputfile()

        MAX_Y = len(lines)
        MAX_X = len(lines[0])

        res_lines = deepcopy(lines)

        for y, line in enumerate(lines):
            for x in range(0, len(line)):
                if line[x] == '@':
                    combinations = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1), (y - 1, x - 1), (y + 1, x + 1), (y - 1, x + 1), (y + 1, x - 1)]
                    combinations = list(filter(lambda elt: elt[1] >= 0 and elt[1] < MAX_X and elt[0] >= 0 and elt[0] < MAX_Y, combinations))
                    rolls = list(map(lambda coordinate: lines[coordinate[0]][coordinate[1]], combinations))
                    rolls = list(filter(lambda case: case == '@', rolls))
                    if len(rolls) < 4:
                        res_lines[y][x] = 'x'
                        result += 1

        return result

    def solve_part2(self):
        result = 0
        lines = self._parse_inputfile()

        MAX_Y = len(lines)
        MAX_X = len(lines[0])

        while True:
            removed_lines = deepcopy(lines)
            removed_rolls = 0
            for y, line in enumerate(lines):
                for x in range(0, len(line)):
                    if line[x] == '@':
                        combinations = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1), (y - 1, x - 1), (y + 1, x + 1), (y - 1, x + 1), (y + 1, x - 1)]
                        combinations = list(filter(lambda elt: elt[1] >= 0 and elt[1] < MAX_X and elt[0] >= 0 and elt[0] < MAX_Y, combinations))
                        rolls = list(map(lambda coordinate: lines[coordinate[0]][coordinate[1]], combinations))
                        rolls = list(filter(lambda case: case == '@', rolls))
                        if len(rolls) < 4:
                            removed_lines[y][x] = '.'
                            removed_rolls += 1
            if removed_rolls == 0: break
            result += removed_rolls
            lines = removed_lines

        return result
