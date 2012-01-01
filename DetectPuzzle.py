#!/usr/bin/python

# Return the picture for use in the Picross Solver
# May return a constant picture or a web camera image
import Image

def detect(picture):
    return None # puzzle grid


# testing main
if __name__=='__main__':
    test_pic = './picture.jpg'
    image = Image.open(test_pic)
    puzzlegrid = DetectPuzzle.detect(image)
    print puzzlegrid


