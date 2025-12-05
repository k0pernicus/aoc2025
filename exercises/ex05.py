from solver import Solver
import logger
from collections import defaultdict
from copy import deepcopy

class Ex05(Solver):
    _RANGES = defaultdict(list)
    _AVAILABLE_INGREDIENTS = []

    def _parse_inputfile(self):
        if len(self._RANGES) > 0 and len(self._AVAILABLE_INGREDIENTS) > 0:
            return self._RANGES, self._AVAILABLE_INGREDIENTS
        available_ingredients = False
        with open(self._input_filepath, 'r') as f:
            for line in f:
                stripped_line = line.strip()
                if not stripped_line and not available_ingredients:
                    available_ingredients = True
                    continue
                if available_ingredients:
                    self._AVAILABLE_INGREDIENTS.append(int(line))
                else:
                    parts = line.split('-')
                    lp, rp = int(parts[0]), int(parts[1])
                    self._RANGES[lp].append(rp)

        return sorted(self._RANGES.items()), self._AVAILABLE_INGREDIENTS

    def solve_part1(self):
        result = 0
        ranges, ingredients = self._parse_inputfile()

        for ingredient in ingredients:
            for (k, v) in ranges:
                if ingredient < k:
                    break
                if len(list(filter(lambda x: x >= ingredient, v))) > 0:
                    result += 1
                    break

        return result

    def solve_part2(self):
        ranges, ingredients = self._parse_inputfile()
        ranges = {k: max(v) for k,v in ranges.items()}

        full_ranges = {}

        for (left_range, right_range) in sorted(ranges.items()):
            found = False
            for (compared_left, compared_right) in sorted(full_ranges.items()):
                if left_range >= compared_left and right_range <= compared_right:
                    # already in the range
                    found = True
                    break
                elif left_range < compared_left and right_range < compared_right:
                    del full_ranges[compared_left]
                    full_ranges[left_range] = compared_right
                    found = True
                    break
                elif left_range >= compared_left and left_range <= compared_right and right_range >= compared_right:
                    full_ranges[compared_left] = right_range
                    found = True
                    break
                elif left_range < compared_left and right_range >= compared_right:
                    del full_ranges[compared_left]
                    break
            if not found:
                full_ranges[left_range] = right_range

        result = sum(map(lambda r: (r[1] - r[0]) + 1, full_ranges.items()))
        return result
