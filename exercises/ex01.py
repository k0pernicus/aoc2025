from solver import Solver
import logger
import os

INIT_POSITION = 50

class Ex01(Solver):
    # Cached parsed input
    _LINES = []

    def _parse_inputfile(self):
        if len(self._LINES) > 0: return self._LINES
        with open(self.input_filepath, 'r') as f:
            for line in f:
                stripped_line = line.strip()
                if not stripped_line: continue
                self._LINES.append(stripped_line)
        return self._LINES


    def solve_part1(self):
        position = INIT_POSITION
        nb_zeroes = 0
        lines = self._parse_inputfile()

        for line in lines:
            mag = int(line[1:])

            dxn = (-1 if line[0] == 'L' else 1)

            position = ((position + dxn * mag) % 100)
            if position == 0: nb_zeroes += 1

            self._logger.log(f'with line of {line} => {position}', level=logger.DEBUG)

        return nb_zeroes

    def solve_part2(self):
        position = INIT_POSITION
        nb_zeroes = 0
        lines = self._parse_inputfile()

        for line in lines:
            mag = int(line[1:])
            (rotations, mag) = (abs(mag) // 100, mag % 100)

            dxn = (-1 if line[0] == 'L' else 1)

            position = position + dxn * mag
            # The current position is outside the range (0-100)
            # and we did not start to 0
            crosses_zero = (0 >= position or position >= 100) and ((position - dxn * mag) % 100 > 0)

            nb_zeroes += rotations + crosses_zero
            position = position % 100

            self._logger.log(f'with line of {line} => {position}', level=logger.DEBUG)

        return nb_zeroes
