#!/usr/bin/python

# Return the picture for use in the Picross Solver
# May return a constant picture or a web camera image
import Image
import ImageShow

def fix_skew(picture):
    return picture # picture


# testing main
if __name__=='__main__':
    test_pic = './testpicture.jpg'
    image = Image.open(test_pic)
    fixed = fix_skew(image)
    ImageShow.show(fixed, 'skew removed')


