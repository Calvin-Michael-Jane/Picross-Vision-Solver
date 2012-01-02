#!/usr/bin/python

# Represents the numbers found that represent the entire puzzle.
# Numbers are found on the `top` and the `side` in 2D arrays.

class PuzzleRep:
    def __init__(self, top, side):
        self.top = top
        self.side = side

# A SolutionRep.solution is a 2D boolean array representing
# which boxes within the puzzle should be filled in.
class SolutionRep:
    def __init__(self, two_d_bool_array):
        self.solution = two_d_bool_array


