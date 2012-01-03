#!/usr/bin/python

# Return the picture for use in the Picross Solver
# May return a constant picture or a web camera image
import Image
import ImageShow

test_pic = './testpicture.jpg'

def picture():
    image = Image.open(test_pic)
    pixels = image.load()
    #for x in range(w):
    #    for y in range(h):
    #        pix = pixels[x, y]
    return image # picture


if __name__=='__main__':
    ImageShow.show(picture(), "window title")



