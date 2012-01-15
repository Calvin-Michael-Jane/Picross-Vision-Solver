#!/usr/bin/python


import Image 
import sys 

 
def prewitt(pixels, width, height): 
    xmask, ymask = get_prewitt_masks() 
 
    # create a new greyscale image for the output 
    outimg = Image.new('L', (width, height)) 
    out_horizontal = Image.new('L', (width, height))
    out_vertical = Image.new('L', (width, height))

    outpixels = list(outimg.getdata())
    out_h_pixels = list(outimg.getdata())
    out_v_pixels = list(outimg.getdata())
 
    for y in xrange(height): 
        for x in xrange(width): 
            sumX, sumY, magnitude = 0, 0, 0 
 
            if y == 0 or y == height-1: magnitude = 0 
            elif x == 0 or x == width-1: magnitude = 0 
            else: 
                for i in xrange(-1, 2): 
                    for j in xrange(-1, 2): 
                        # convolve the image pixels with the Prewitt mask, approximating &#8706;I / &#8706;x 
                        sumX += (pixels[x+i+(y+j)*width]) * xmask[i+1, j+1] 
 
                for i in xrange(-1, 2): 
                    for j in xrange(-1, 2): 
                        # convolve the image pixels with the Prewitt mask, approximating &#8706;I / &#8706;y 
                        sumY += (pixels[x+i+(y+j)*width]) * ymask[i+1, j+1] 
 
            # approximate the magnitude of the gradient 
            magnitude = abs(sumX) + abs(sumY) 
 
            magH = abs(sumX)
            magV = abs(sumY)

            if magnitude > 255: magnitude = 255 
            if magnitude < 0: magnitude = 0

            if abs(sumX) > 175: magH = 255
            if abs(sumX) < 0: magH = 0

            if abs(sumY) > 175: magV = 175
            if abs(sumY) < 0: magV = 0
 
            outpixels[x+y*width] = 255 - magnitude 
            out_h_pixels[x+y*width] = 255 - magH
            out_v_pixels[x+y*width] = 255 - magV
 
    outimg.putdata(outpixels)
    out_horizontal.putdata(out_h_pixels)
    out_vertical.putdata(out_v_pixels)
    return (outimg, out_horizontal, out_vertical) 


# Uses hashes of tuples to simulate 2-d arrays for the masks. 
def get_prewitt_masks(): 
    xmask = {} 
    ymask = {} 
 
    xmask[(0,0)] = -1 
    xmask[(0,1)] = 0 
    xmask[(0,2)] = 1 
    xmask[(1,0)] = -1 
    xmask[(1,1)] = 0 
    xmask[(1,2)] = 1 
    xmask[(2,0)] = -1 
    xmask[(2,1)] = 0 
    xmask[(2,2)] = 1 
 
    ymask[(0,0)] = 1 
    ymask[(0,1)] = 1 
    ymask[(0,2)] = 1 
    ymask[(1,0)] = 0 
    ymask[(1,1)] = 0 
    ymask[(1,2)] = 0 
    ymask[(2,0)] = -1 
    ymask[(2,1)] = -1 
    ymask[(2,2)] = -1 
    return (xmask, ymask)

if __name__ == '__main__': 
    img = Image.open(sys.argv[1]) 
    # only operates on greyscale images 
    if img.mode != 'L': img = img.convert('L') 
    pixels = list(img.getdata()) 
    w, h = img.size 
    (outimg, outh, outv) = prewitt(pixels, w, h) 
    outimg.save(sys.argv[2]+".jpg")
    outh.save(sys.argv[2]+"_h.jpg")
    outv.save(sys.argv[2]+"_v.jpg")

