from solver import Solver
from collections import Counter
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
        ranges = self._parse_inputfile()
        res = 0

        interest_list = set()

        self._logger.log("Hum hum... YOLO (2)!!!", logger.DEBUG)

        # collect the interesting values
        for r in ranges:
            il, ir = int(r[0]), int(r[1])
            d = il
            while d <= ir:
                sd = str(d)
                if len(sd) > 1:
                    c = Counter(sd)
                    if len(set(c.values())) == 1 or all([x % 2 == 0 for x in c.values()]):
                        interest_list.add(sd)
                d += 1

        # find the common stuff
        for value in interest_list:
            if len(Counter(value).keys()) == 1:
                res += int(value)
                continue
            d = 1
            while d <= (len(value) // 2):
                c = value
                f, c = c[:d], c[d:]
                while len(c) > 0:
                    t = c[:d]
                    if t == f:
                        c = c[d:]
                        continue
                    else:
                        break
                if len(c) == 0:
                    res += int(value)
                    break
                d += 1

        return res
