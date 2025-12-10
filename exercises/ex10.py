from solver import Solver
import logger
from collections import deque
from typing import List, Set
from functools import reduce

class Ex10(Solver):
    _PUZZLES: List[Set] = []
    _BUTTONS: List[List[Set]] = []
    _VOLTS: List[List[int]] = []

    def parse_file(self):
        if len(self._PUZZLES) > 0: return (self._PUZZLES, self._BUTTONS, self._VOLTS)
        with open(self._input_filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if not line: continue
                parts = line.split()
                self._PUZZLES.append(set([i for i, c in enumerate(parts[0][1:-1]) if c == '#']))  # [.##.]
                self._BUTTONS.append([])
                for part in parts[1:]:
                    if part[0] == '(': # Button - (1,3)
                        buttons = part[1:-1].split(',')
                        self._BUTTONS[-1].append(set(map(int, buttons)))
                    elif part[0] == '{': # Volt - {3,5,4,7}
                        volts = part[1:-1].split(',')
                        self._VOLTS.append(list(map(int, volts)))
                    else: raise Exception("error parsing the object")
        return (self._PUZZLES, self._BUTTONS, self._VOLTS)

    def solve_part1(self):


# count = 0
# for machine in machines:
#     init = 0
#     visited = {init}
#     queue = deque([(init, 0)])
#     while queue:
#         prev, n = queue.popleft()
#         if prev == machine.lights:
#             count += n
#             break
#         for b in machine.buttons:
#             xor = prev ^ b
#             if xor not in visited:
#                 visited.add(xor)
#                 queue.append((xor, n + 1))

        puzzles, buttons, volts = self.parse_file()
        result = 0

        for (i, puzzle) in enumerate(puzzles):
            init = frozenset()
            queue = deque([(init, 0)])
            visited = {frozenset()}
            while queue:
                prev, presses = queue.popleft()
                if prev == puzzle:
                    result += presses
                    break
                for button in buttons[i]:
                    xor = prev ^ button
                    if xor not in visited:
                        visited.add(xor)
                        queue.append((xor, presses + 1))

        return result

    def solve_part2(self):
        puzzles, buttons, volts = self.parse_file()

        result = 0

        return result
