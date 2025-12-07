from solver import Solver
import logger
from collections import defaultdict
from typing import Set

class Ex07(Solver):

    def solve_part1(self):
        result = 0
        splits = defaultdict(set) # {y: x}

        with open(self._input_filepath, 'r') as f:
            lines = f.readlines()
            # find the 'S' position
            first_positions = [pos for pos, c in enumerate(lines[0]) if lines[0][pos] == 'S']
            assert(len(first_positions) == 1)
            splits[1] = set([first_positions[0]])
            y = 1
            for line in lines[1:]:
                vertical_splits: Set(int) = splits[y]
                splitters = set([pos for pos, c in enumerate(lines[y]) if lines[y][pos] == '^'])
                stops = splitters.intersection(vertical_splits)
                result += len(stops)
                continues = vertical_splits.difference(splitters)
                y += 1
                splits[y] = set(continues).union(set(map(lambda x: x - 1, stops))).union(set(map(lambda x: x + 1, stops)))

        return result

    def solve_part2(self):
        with open(self._input_filepath, 'r') as f:
            lines = f.readlines()
        
        start = lines[0].find('S')
        counts_per_level = {start: 1}
        Y = len(lines)

        # O(n) algorithm => follow the tree line by line,
        # and count the number of paths until it reaches the leaves
        for y in range(Y):
            new_counts = defaultdict(int)
            for x, count in counts_per_level.items():
                if lines[y][x] == '^':
                    new_counts[x-1] += count
                    new_counts[x+1] += count
                else:
                    new_counts[x] += count
            counts_per_level = new_counts
        return sum(counts_per_level.values())
