from solver import Solver
import logger
import os
from collections import Counter

class Ex03(Solver):
    # Cached parsed input
    _LINES = []

    def _parse_inputfile(self):
        if len(self._LINES) > 0: return self._LINES
        with open(self._input_filepath, 'r') as f:
            for line in f:
                stripped_line = line.strip()
                if not stripped_line: continue
                self._LINES.append(stripped_line)
        return self._LINES

    def solve_part1(self):
        s = 0
        lines = self._parse_inputfile()

        for line in lines:
            highest_nb = int(line[-2:])
            cp, hr = len(line) - 2, len(line) - 1
            while cp >= 0:
                cn = (int(line[cp]) * 10 + int(line[hr]))
                if cn > highest_nb: highest_nb = cn
                if int(line[hr]) < int(line[cp]): hr = cp
                cp -= 1
            s += highest_nb

        return s

    def solve_part2(self):
        s = 0
        lines = self._parse_inputfile()

        MAX_LEN = 12

        for line in lines:
            lifo = [line[0]]
            rest = list(line[:1])

            while len(rest) > 0:
                to_compare = rest.pop(0)
                if (to_compare < lifo[-1]) and (len(rest) + len(lifo) <= MAX_LEN):
                    lifo.append(to_compare)
                    continue
                while (len(lifo) > 0) and (lifo[-1] < to_compare) and (len(rest) + len(lifo) >= MAX_LEN):
                    lifo.pop(-1)
                lifo.append(to_compare)

            s += int(''.join([str(x) for x in lifo[:MAX_LEN]]))

        return s
