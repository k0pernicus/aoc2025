from solver import Solver
import logger
import os

class Ex02(Solver):
    # Cached parsed input
    _INPUTS = []

    def _parse_inputfile(self):
        if len(self._INPUTS) > 0: return self._INPUTS
        with open(self._input_filepath, 'r') as f:
            for line in f:
                parts = line.split(',')
                for part in parts:
                    r = part.split('-')
                    if len(r) < 2: continue
                    self._INPUTS.append((r[0], r[1]))
        return self._INPUTS


    def solve_part1(self):
        ranges = self._parse_inputfile()
        res = 0

        self._logger.log("Hum hum... YOLO!!!", logger.DEBUG)

        for r in ranges:
            il, ir = int(r[0]), int(r[1])
            d = il
            while d <= ir:
                sd = str(d)
                ld = len(sd)
                if ld % 2 == 0 and sd[ : ld // 2] == sd[ld // 2 : ]:
                    res += d
                d += 1

        return res

    def solve_part2(self):
        lines = self._parse_inputfile()

        return 0
