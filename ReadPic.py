#!/usr/bin/python

import Image, ImageFilter

if __name__=='__main__':
  image = Image.open('./snapshot.jpg')
  image.filter(ImageFilter.FIND_EDGES).save("./snapshot_e.jpg")



