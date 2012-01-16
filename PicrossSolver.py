#!/usr/bin/python

# Return the solution to the puzzle given as input.
# Solution is a SolutionRep. Puzzle is a PuzzleRep
# A SolutionRep.solution should be a 2D Boolean array

# Implements http://www.liacs.nl/~kosters/buffalo.pdf

import Image
import Representations

def solve(puzzle):
    side = puzzle.side
    top = puzzle.top
    puzzle = to_notation(puzzle);
    two_d_boolean_array = [[0] * len(top)] * len(side);
    two_d_boolean_array[3][4] = 1
    two_d_boolean_array[2][1] = 1
    solution = Representations.SolutionRep(two_d_boolean_array)
    return solution # puzzle solution representation
    
def to_notation(puzzle):
    top = []
    side = []
    for a in puzzle.top:
        if a[0] == 0:
            top.append([[0, len(puzzle.top), len(puzzle.top)]])
        else:
            col = [[0, 0, float('inf')]]
            for x in a[:-1]:
                col.append([1, x, x])
                col.append([0, 0, float('inf')])
            col.append([1, a[-1], a[-1]])
            col.append([0, 0, float('inf')])
            top.append(col)
    for a in puzzle.side:
        if a[0] == 0:
            side.append([[0, len(puzzle.side), len(puzzle.side)]])
        else:
            row = [[0, 0, float('inf')]]
            for x in a[:-1]:
                row.append([1, x, x]);
                row.append([0, 0, float('inf')])
            row.append([1, a[-1], a[-1]])
            row.append([0, 0, float('inf')])
            side.append(col)
    puzzle.top = top;
    puzzle.side = side;
    return puzzle


   
#   The boolean function Fix(s, d) is true iff s is fixable with respect to d.
def fix(i, j, s, d):
    A_jprev = 0 ###########
    B_jprev = 0 ########### 
    if i == 0 and A_j == 0:
        return true
    if j == 0:
        return false
    if i < A_j or i > B_j:
        return false
    # let L_sig_i(s) denote the largest index h < i such that s_h != sig and s_h != x, or 0.
    min(i-a_j, B_jprev)
    p = max(i-b_j, A_jprev, L)
    fix(p, j-1, s, d)

#   The Settle operation produces, given a string s over T and a description d, the 
#   string where all string elements that have the same value in every fix are set    
def settle():  
    hi = 0

# testing main
if __name__=='__main__':
    test_pic = './images/testpicture.jpg'
    image = Image.open(test_pic)
    # x = [[0], [5, 2], [3]]
    top = [[0], [5], [2, 2], [5, 2], [7], [2, 5], [2, 7], [1, 8], [7], [5]]
    side = [[2], [2], [2, 1, 2], [4, 4], [1, 7], [1, 7], [1, 7], [2, 6], [7], [2, 2]]
    temp_puzzle = Representations.PuzzleRep(top, side)
    solution = solve(temp_puzzle)
    # print solution

