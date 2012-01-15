#!/usr/bin/python

import Image
from math import sqrt
from math import floor

i = Image.open(p);
print i.format
print i.size
print i.mode
pix = i.load()
j = Image.new("RGB",i.size);
pix2 = j.load();
for a in range(1,i.size[0]):
 for b in range(1,i.size[1]):
  value = 0
  for c in range(0,3):
   value += (pix[a,b][c] - pix[a,b-1][c]) ** 2
   value += (pix[a,b][c] - pix[a-1,b][c]) ** 2

  value = floor(sqrt(value))
  pix2[a,b] = (value,value,value);

j.save("test.bmp");

