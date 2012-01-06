#!/usr/bin/python

# Return the picture for use in the Picross Solver
# May return a constant picture or a web camera image
import Image
import Representations

def detect(picture):
    grid = [(0,0),(1,0),(1,1),(0,1)]; # grid corners
    cell_length = 0;
    gr = Representations.GridRep(grid, cell_length)
    return gr # grid representation


# testing main
if __name__=='__main__':
    test_pic = './testpicture.jpg'
    image = Image.open(test_pic)
    puzzlegrid = detect(image)
    print 'grid: ',
    print puzzlegrid.grid
    print 'cell length: ',
    print puzzlegrid.cell_length


