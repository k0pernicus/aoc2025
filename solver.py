from abc import ABC, abstractmethod
from logger import Logger

class Solver(ABC):
    def __init__(self, input_filepath, debug_logs):
        self._input_filepath = input_filepath
        self._logger = Logger(show_debug=debug_logs)

    @abstractmethod
    def solve_part1(self):
        pass

    @abstractmethod
    def solve_part2(self):
        pass
