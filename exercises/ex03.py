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

        MAX_LEN = 11

        for line in lines:
            # print(f"> current line is {line}")
            fw = []
            bl, br = line[:-MAX_LEN], line[-MAX_LEN:]
            # Find the first highest in bl !
            lidx = 0
            ridx = 0
            hc = 0
            for i, c in enumerate(bl):
                if int(c) > hc:
                    hc = int(c)
                    lidx = i + 1
            fw.append(str(hc))
            # Now that we found the highest, we can compare with the rest of the word
            while len(fw) < (MAX_LEN + 1):
                bl = line[lidx:-MAX_LEN-1]
                br = line[ridx-MAX_LEN:-MAX_LEN++len(fw)] if len(fw) < MAX_LEN else line[-MAX_LEN+ridx:]
                # print(f"fw is {fw}\nbl is {bl}\nbr is {br}")
                hc = 0
                clidx = lidx
                # find the next highest value
                for i, c in enumerate(bl):
                    if int(c) > hc:
                        hc = int(c)
                        clidx = i + lidx
                # print(f">> found highest left value at {hc}, idx {clidx} (ridx is {ridx})")
                hr = 0
                cridx = ridx
                for i, c in enumerate(br):
                    if int(c) > hr:
                        hr = int(c)
                        cridx = i + ridx
                if hc < hr:
                    fw.append(str(hr))
                    ridx = cridx + 1
                else:
                    fw.append(str(hc))
                    lidx = clidx + 1

            print(f"FOUND FW WITH VALUE {''.join(fw)}")
            s += int(''.join(fw))

        return s
