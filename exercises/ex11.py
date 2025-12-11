from solver import Solver
import logger
from collections import defaultdict, deque
from typing import Set
import itertools

class Ex11(Solver):
    _PATHS = defaultdict(Set[str])

    def parse_file(self):
        if len(self._PATHS) > 0: return self._PATHS
        with open(self._input_filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if not line: continue
                [input, outputs] = line.split(':')
                self._PATHS[input] = outputs.split()
        return self._PATHS

    def solve_part1(self):
        paths = self.parse_file()
        end_paths = []

        def dfs(input, visited): 
            if input == 'out':
                end_paths.append(visited)
                return
            if input in visited:
                return
            for output in self._PATHS[input]:
                dfs(output, visited ^ {input})

        dfs('you', set())

        return len(end_paths)

    def solve_part2(self):
        paths = self.parse_file()
        result = 0

        return result
