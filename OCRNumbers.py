#!/usr/bin/python

# Return the picture for use in the Picross Solver
# May return a constant picture or a web camera image
import Image
import Representations

puzzle_size = 5

def ocr(num_pos, picture):
    top = [[0]*puzzle_size for x in xrange(puzzle_size)] #2D array
    side = [[0]*puzzle_size for x in xrange(puzzle_size)]
    pr = Representations.PuzzleRep(top, side) # consists of side and top 2D arrays
    return pr # puzzle representation

# i write neural network now l0l

# testing main
if __name__=='__main__':
    test_pic = './images/testpicture.jpg'
    image = Image.open(test_pic)
    number_positions = [(0,0), (1,1)]
    puzzle = ocr(number_positions, image)
    print 'top: ',
    print puzzle.top
    print 'side: ',
    print puzzle.side


