#!/usr/bin/python

# Return the input picture after being processed for skew
# by checking to see the orientation of the strongest lines
# using line detection. Uses Hough Transformation.
import Image
import ImageShow
import ImageDraw
import math

def fix_skew(picture):
    accumulator = {} # (theta, rho): num_votes
    found_points = {}
    rotation = 0;
    
    # convert image to grayscale array
    grayscale_picture = picture.convert("L")
    pixels = grayscale_picture.load()
    
    # traverse pixels in image to vote
    width, height = picture.size
    
    THRES_BLACK = 20
    
    for x in range(width):
        for y in range(height):
            # check if pixel is "black"
            if pixels[x, y] < THRES_BLACK:
                # 180 lines through (x, y), vote
                THETA_RANGE = 10
                for theta in range(-1 * THETA_RANGE, THETA_RANGE):
                    rho = math.floor(x * math.cos(theta) + y * math.sin(theta))
                    if rho < 0: 
                        continue
                    ac_key = (theta, rho)
                    if ac_key not in accumulator:
                        accumulator[ac_key] = 1
                        found_points[ac_key] = []
                    else:
                        accumulator[ac_key] += 1
                    found_points[ac_key].append((x, y))
    
    # find (theta, rho) with most votes
    max_votes = 0
    max_key = 0 #(0,0)
    
    for key in accumulator:
        if accumulator[key] > max_votes:
            max_votes = accumulator[key] # num_votes
            max_key = key
        if accumulator[key] > 10:
            print 'key: {0} {1}'.format(key, accumulator[key])
    
    print max_votes
    print max_key
    
    # draw points associated with max key
    draw = ImageDraw.Draw(picture)
    BOXSIZE = 3
    for point in found_points[max_key]:
        ptx = point[0]
        pty = point[1]
        draw.rectangle([ptx-BOXSIZE, pty-BOXSIZE, ptx+BOXSIZE, pty+BOXSIZE], fill=128)
    del draw
    ImageShow.show(picture, 'with points')
    
    # perform rotation & composite to make bkg white
    # source: http://stackoverflow.com/questions/5252170/
    # specify-image-filling-color-when-rotating-in-python-with-pil-and-setting-expand
    picture = picture.convert('RGBA')
    picture = picture.rotate(max_key[0], expand=True)
    white = Image.new('RGBA', picture.size, (255,)*4)
    picture = Image.composite(picture, white, picture)
    
    return picture # picture


# testing main
if __name__=='__main__':
    test_pic = './blue_9.jpg'
    image = Image.open(test_pic)
    fixed = fix_skew(image)
    ImageShow.show(fixed, 'skew removed')


