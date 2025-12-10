from solver import Solver
import logger
from collections import defaultdict

class Ex09(Solver):
    _POINTS_COORDINATES = []

    def parse_file(self):
        if len(self._POINTS_COORDINATES) > 0: return self._POINTS_COORDINATES
        with open(self._input_filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if not line: continue
                x, y = line.split(',')
                x, y = int(x), int(y)
                self._POINTS_COORDINATES.append((x, y))
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

        # Coordinate Compression
        unique_x = sorted(list(set(c[0] for c in coordinates)))
        unique_y = sorted(list(set(c[1] for c in coordinates)))

        # Maps to convert Real Coordinate -> Compressed Index
        map_x = {x: i for i, x in enumerate(unique_x)}
        map_y = {y: i for i, y in enumerate(unique_y)}

        # The compressed grid dimensions
        W = len(unique_x) - 1
        H = len(unique_y) - 1

        grid = [[0] * W for _ in range(H)]

        # Identify Vertical Edges of the Polygon
        v_edges = []
        num_points = len(coordinates)
        for k in range(num_points):
            p1 = coordinates[k]
            p2 = coordinates[(k + 1) % num_points]

            if p1[0] == p2[0]:
                x = p1[0]
                min_y = min(p1[1], p2[1])
                max_y = max(p1[1], p2[1])
                v_edges.append((x, min_y, max_y))

        # Fill the Compressed Grid (Scan Line / Even-Odd Rule)
        for j in range(H):
            y_start = unique_y[j]
            y_end = unique_y[j+1]

            active_edges = [edge_x for edge_x, edge_ymin, edge_ymax in v_edges
                            if edge_ymin <= y_start and edge_ymax >= y_end]
            active_edges.sort()

            for e in range(0, len(active_edges), 2):
                x_left = active_edges[e]
                x_right = active_edges[e+1]

                idx_start = map_x[x_left]
                idx_end = map_x[x_right]

                for i in range(idx_start, idx_end):
                    grid[j][i] = 1

        # Build 2D Prefix Sum (Integral Image) on the Compressed Grid
        prefix = [[0] * (W + 1) for _ in range(H + 1)]
        for y in range(H):
            for x in range(W):
                prefix[y+1][x+1] = (grid[y][x] + prefix[y][x+1] + prefix[y+1][x] - prefix[y][x])

        def get_compressed_sum(cx1, cy1, cx2, cy2):
            # Standard inclusion-exclusion principle
            x_min, x_max = min(cx1, cx2), max(cx1, cx2)
            y_min, y_max = min(cy1, cy2), max(cy1, cy2)
            return (prefix[y_max][x_max] - prefix[y_min][x_max] - prefix[y_max][x_min] + prefix[y_min][x_min])

        result = 0
        for i in range(len(coordinates)):
            x1, y1 = coordinates[i]
            cx1, cy1 = map_x[x1], map_y[y1]

            for j in range(i + 1, len(coordinates)):
                x2, y2 = coordinates[j]

                width = abs(x1 - x2) + 1
                height = abs(y1 - y2) + 1
                area = width * height

                if area <= result:
                    continue

                cx2, cy2 = map_x[x2], map_y[y2]

                blocks_wide = abs(cx1 - cx2)
                blocks_high = abs(cy1 - cy2)
                expected_sum = blocks_wide * blocks_high

                actual_sum = get_compressed_sum(cx1, cy1, cx2, cy2)

                if actual_sum == expected_sum:
                    result = area

        return result
