from solver import Solver
import logger
from collections import defaultdict
from typing import Set
from math import sqrt, pow

class Ex08(Solver):
    _LINES = []

    def parse_file(self):
        if len(self._LINES) > 0: return self._LINES
        with open(self._input_filepath, 'r') as f:
            lines = f.readlines()
        self._LINES = [(0, 0, 0) for _ in range(len(lines))]
        for i, line in enumerate(lines):
            line = line.strip()
            if not line: continue
            x, y, z = line.split(',')
            x, y, z = int(x), int(y), int(z)
            self._LINES[i] = (x, y, z)
        return self._LINES

    def solve_part1(self):
        coordinates = self.parse_file()

        distances = defaultdict(int)
        junctions = []
        for i, coordinate in enumerate(coordinates):
            for compared_coordinate in coordinates[i+1:]:
                x1, y1, z1 = coordinate
                x2, y2, z2 = compared_coordinate
                distances[f"{coordinate}+{compared_coordinate}"] = sqrt((pow(x1 - x2, 2)) + (pow(y1 - y2, 2)) + (pow(z1 - z2, 2)))

        sorted_distances = sorted(distances.items(), key=lambda x: x[1], reverse=False)
        distances = dict(sorted_distances)

        for min_distance_box in sorted_distances[:1000]:
            box1, box2 = min_distance_box[0].split('+')
            found_box1, found_box2 = None, None
            for i, junction in enumerate(junctions):
                if box1 in junction: found_box1 = i
                if box2 in junction: found_box2 = i
                if found_box1 and found_box2: break
            if found_box1 is None and found_box2 is None:
                junctions.append(set([box1, box2]))
            elif found_box1 is None and found_box2 is not None:
                junctions[found_box2].add(box1)
            elif found_box1 is not None and found_box2 is None:
                junctions[found_box1].add(box2)
            elif found_box1 is not None and found_box2 is not None and found_box1 != found_box2:
                junctions[found_box1] = junctions[found_box1].union(junctions[found_box2])
                del junctions[found_box2]

        sorted_result = sorted(junctions, key=lambda x: len(x), reverse=True)
        return len(sorted_result[0]) * len(sorted_result[1]) * len(sorted_result[2])

    def solve_part2(self):
        coordinates = self.parse_file()

        distances = defaultdict(int)
        junctions = []
        for i, coordinate in enumerate(coordinates):
            for compared_coordinate in coordinates[i+1:]:
                x1, y1, z1 = coordinate
                x2, y2, z2 = compared_coordinate
                distances[f"{coordinate}+{compared_coordinate}"] = sqrt((pow(x1 - x2, 2)) + (pow(y1 - y2, 2)) + (pow(z1 - z2, 2)))

        sorted_distances = sorted(distances.items(), key=lambda x: x[1], reverse=False)
        distances = dict(sorted_distances)

        last_junction = None

        for min_distance_box in sorted_distances:
            box1, box2 = min_distance_box[0].split('+')
            found_box1, found_box2 = None, None
            for i, junction in enumerate(junctions):
                if box1 in junction: found_box1 = i
                if box2 in junction: found_box2 = i
                if found_box1 and found_box2: break
            if found_box1 is None and found_box2 is None:
                junctions.append(set([box1, box2]))
                last_junction = (box1, box2)
            elif found_box1 is None and found_box2 is not None:
                junctions[found_box2].add(box1)
                last_junction = (box1, box2)
            elif found_box1 is not None and found_box2 is None:
                junctions[found_box1].add(box2)
                last_junction = (box1, box2)
            elif found_box1 is not None and found_box2 is not None and found_box1 != found_box2:
                junctions[found_box1] = junctions[found_box1].union(junctions[found_box2])
                del junctions[found_box2]
                last_junction = (box1, box2)

        (x1, _, _) = last_junction[0][1:-1].split(',')
        (x2, _, _) = last_junction[1][1:-1].split(',')

        return int(x1) * int(x2)
