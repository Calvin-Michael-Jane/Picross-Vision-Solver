#!/usr/bin/python

# Represents the numbers found that represent the entire puzzle.
# Numbers are found on the `top` and the `side` in 2D arrays.
class PuzzleRep:
    def __init__(self, top, side):
        self.top = top
        self.side = side

# Represents grid cells with numbers, determined by FindNumbers.
# DigitsRep.top and DigitsRep.side are each lists of lists where 
# each sublist has the same x or y coord respectively.
class DigitsRep:
    def __init__(self, top, side):
        self.top = top
        self.side = side
        
# Represents dimensions of grid determined by DetectGrid.
# A GridRep.grid is an array of coordinates of the image grid corners.
# GridRep.cell_length is the length of the grid squares.
class GridRep:
    def __init__(self, grid, x_coords, y_coords, cell_width, cell_height):
        self.grid = grid
        self.x_coords = x_coords
        self.y_coords = y_coords
        self.cell_width = cell_width
        self.cell_height = cell_height

# A SolutionRep.solution is a 2D boolean array representing
# which boxes within the puzzle should be filled in.
class SolutionRep:
    def __init__(self, two_d_bool_array):
        self.solution = two_d_bool_array


