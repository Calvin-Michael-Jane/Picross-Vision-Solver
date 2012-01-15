#!/usr/bin/python

import Image
import ImageFilter

image = Image.open('./red.jpg')
bw = image.convert("L")
bw.save("bw.jpg")

image.filter(ImageFilter.SMOOTH).save("red_smooth.jpg")
image.filter(ImageFilter.EDGE_ENHANCE).save("red_ee.jpg")
image.filter(ImageFilter.EDGE_ENHANCE_MORE).save("red_mee.jpg")
image.filter(ImageFilter.FIND_EDGES).save("red_fe.jpg")

bw.filter(ImageFilter.SMOOTH).save("bw_smooth.jpg")
bw.filter(ImageFilter.EDGE_ENHANCE).save("bw_ee.jpg")
bw.filter(ImageFilter.EDGE_ENHANCE_MORE).save("bw_mee.jpg")
bw.filter(ImageFilter.FIND_EDGES).save("bw_fe.jpg")



