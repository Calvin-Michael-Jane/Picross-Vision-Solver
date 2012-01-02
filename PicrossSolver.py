#!/usr/bin/python

# Return the solution to the puzzle given as input.
# Solution is a SolutionRep. Puzzle is a PuzzleRep
# A SolutionRep.solution should be a 2D Boolean array
import Image
import Representations

def solve(puzzle):
    side = puzzle.side
    top = puzzle.top
    two_d_boolean_array = top
    solution = Representations.SolutionRep(two_d_boolean_array)
    return solution # puzzle solution representation


# testing main
if __name__=='__main__':
    test_pic = './testpicture.jpg'
    image = Image.open(test_pic)
    top = [[0,0],[0,0]]
    side = [[1,1],[1,1]]
    temp_puzzle = Representations.PuzzleRep(top, side)
    solution = solve(temp_puzzle)
    print solution.solution


