from solver import Solver
import logger

class Ex09(Solver):
    _POINTS_COORDINATES = []

    def parse_file(self):
        if len(self._POINTS_COORDINATES) > 0: return self._POINTS_COORDINATES
        with open(self._input_filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if not line: continue
                x, y = line.split(',')
                self._POINTS_COORDINATES.append((int(x), int(y)))
        return self._POINTS_COORDINATES

    def solve_part1(self):
        coordinates = self.parse_file()

        result = 0
        for i in range(len(coordinates)):
            x1, y1 = coordinates[i]
            for j in range(i, len(coordinates)):
                x2, y2 = coordinates[j]
                compute = (1 + (x1 - x2 if x1 >= x2 else x2 - x1)) * (1 + (y1 - y2 if y1 >= y2 else y2 - y1))
                result = max(result, compute)

        return result

    def solve_part2(self):
        coordinates = self.parse_file()

        return 0
