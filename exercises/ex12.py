from solver import Solver
import logger
from collections import defaultdict, deque
from typing import Set
import functools

class Region(object):
    _WIDTH = 0
    _HEIGHT = 0
    _PLACEMENTS = []

    def __init__(self, dimensions: (int, int), placements: [int]):
        self._WIDTH = dimensions[0]
        self._HEIGHT = dimensions[1]
        self._PLACEMENTS = placements

    def can_fit(self, shapes) -> bool:
        available_area = self._WIDTH * self._HEIGHT
        needed = sum([shapes[i] * self._PLACEMENTS[i] for i in range(len(self._PLACEMENTS))])
        return needed <= available_area

class Ex12(Solver):
    _SHAPES = []
    _REGIONS = []

    def parse_file(self):
        if len(self._SHAPES) > 0 and len(self._REGIONS) > 0: return (self._SHAPES, self._REGIONS)
        with open(self._input_filepath, 'r') as f:
            in_shape = False
            nb_cases = 0
            for line in f:
                line = line.strip()
                if in_shape and line:
                    nb_cases += line.count('#')
                    continue
                if in_shape and not line:
                    in_shape = False
                    self._SHAPES.append(nb_cases)
                    nb_cases = 0
                    continue
                if not line:  continue
                if ':' in line and not 'x' in line:
                    in_shape = True
                    continue
                if 'x' in line:
                    [dimensions, placements] = line.split(':')
                    [w, h] = list(map(int, dimensions.split('x')))
                    placements = list(map(int, placements.strip().split()))
                    self._REGIONS.append(Region((w,h), placements))
        return (self._SHAPES, self._REGIONS)

    def solve_part1(self):
        shapes, regions = self.parse_file()

        valid_regions = 0
        for region in regions:
            if region.can_fit(shapes): valid_regions += 1

        return valid_regions

    def solve_part2(self):
        return "Congratulations, you did it!!"
