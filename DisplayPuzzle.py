#!/usr/bin/python

# Return the picture for use in the Picross Solver
# May return a constant picture or a web camera image
import Image
import Representations

puzzle_size = 5

def visualize(solution):
    print solution.solution


# testing main
if __name__=='__main__':
    test_pic = './images/testpicture.jpg'
    image = Image.open(test_pic)
    answer = [[0]*puzzle_size for x in xrange(puzzle_size)]
    solution = Representations.SolutionRep(answer)
    visualize(solution)

