#!/usr/bin/python

# Return the picture for use in the Picross Solver
# May return a constant picture or a web camera image
import Image

def fix_skew(picture):
    return picture # picture


# testing main
if __name__=='__main__':
    test_pic = './picture.jpg'
    image = Image.open(test_pic)
    AntiSkew.fix_skew(image).show



