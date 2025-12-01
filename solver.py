# base.py
from abc import ABC, abstractmethod

class Solver(ABC):
    def __init__(self, input_filepath):
        self.input_filepath = input_filepath

    @abstractmethod
    def solve_part1(self):
        pass

    @abstractmethod
    def solve_part2(self):
        pass
