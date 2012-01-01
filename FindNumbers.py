#!/usr/bin/python

# Return the picture for use in the Picross Solver
# May return a constant picture or a web camera image
from PIL import Image
import DetectPuzzle

def find_numbers(puzzlegrid, skewless_picture):
    return [(0,0), (1,1)]# number positions


# testing main
if __name__=='__main__':
    test_pic = './testpicture.jpg'
    image = Image.open(test_pic)
    puzzlegrid = DetectPuzzle.detect(image)
    FindNumbers.find_numbers(puzzlegrid, image)



