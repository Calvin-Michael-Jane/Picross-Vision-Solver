#!/usr/bin/python

# Return the picture for use in the Picross Solver
# May return a constant picture or a web camera image
import Image
import ImageShow

#test_pic = './testpicture.jpg'
<<<<<<< HEAD
<<<<<<< HEAD
test_pic = './images/webcam.jpg'
=======
test_pic = './images/blue_9.jpg'
>>>>>>> 00af2da0ba32f069db6b9bff472f7a46ae56466c
=======
test_pic = './images/blue_9.jpg'
>>>>>>> 00af2da0ba32f069db6b9bff472f7a46ae56466c

def picture():
    image = Image.open(test_pic)
    
    # flip along vertical axis
    image = image.transpose(Image.FLIP_LEFT_RIGHT)
    
    return image # picture


if __name__=='__main__':
    ImageShow.show(picture(), "window title")



