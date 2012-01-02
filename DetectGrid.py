#!/usr/bin/python

# Return the picture for use in the Picross Solver
# May return a constant picture or a web camera image
import Image

def detect(picture):
    return [(0,0),(1,0),(1,1),(0,1)] # puzzle grid


# testing main
if __name__=='__main__':
    test_pic = './testpicture.jpg'
    image = Image.open(test_pic)
    puzzlegrid = detect(image)
    print puzzlegrid


