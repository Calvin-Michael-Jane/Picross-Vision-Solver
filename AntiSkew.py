#!/usr/bin/python

# Return the input picture after being processed for skew
# by checking to see the orientation of the strongest lines
# using line detection.
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


