from solver import Solver
import logger
from collections import defaultdict, deque
from typing import Set
import functools

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

        def dfs(node, visited): 
            if node == 'out': return 1
            if node in visited: return 0
            total_paths = 0
            for output in self._PATHS[node]:
                total_paths += dfs(output, visited ^ {node})
            return total_paths

        return dfs('you', set())

    def solve_part2(self):
        paths = self.parse_file()

        @functools.lru_cache(maxsize=None)
        def count_paths_from(node, found_fft, found_dac):
            if node == 'fft': found_fft = True
            elif node == 'dac': found_dac = True
            
            if node == 'out': return 1 if (found_fft and found_dac) else 0
            
            total_paths = 0
            for neighbor in paths[node]:
                total_paths += count_paths_from(neighbor, found_fft, found_dac)
            
            return total_paths

        return count_paths_from('svr', False, False)
