#!/usr/bin/python

# Return the picture for use in the Picross Solver
# May return a constant picture or a web camera image
import Image
import DetectGrid

def find_numbers(puzzlegrid, skewless_picture):
    return [(0,0), (1,1)] # number positions


# testing main
if __name__=='__main__':
    test_pic = './testpicture.jpg'
    image = Image.open(test_pic)
    puzzlegrid = DetectGrid.detect(image)
    nums = find_numbers(puzzlegrid, image)
    print nums


