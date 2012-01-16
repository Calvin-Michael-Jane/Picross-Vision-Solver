#!/usr/bin/python

# Return the picture for use in the Picross Solver
# May return a constant picture or a web camera image
import Image
import ImageShow
import ImageDraw
import prewitt

#test_pic = './testpicture.jpg'
#test_pic = './images/webcam.jpg'
DRAW = False

def picture(pic_name, test_pic):
    image = Image.open(test_pic)
    
    # flip along vertical axis
    image = image.transpose(Image.FLIP_LEFT_RIGHT)
    
    # preprocess: trim to game screen
    image = image.convert('L')
    pixels = list(image.getdata())
    
    width, height = image.size
    (both, hor_filt, vert_filt) = prewitt.prewitt(pixels, width, height)
    
    prewitt_pixels = both.load()
    
    # edge detect on "both" with very high threshold for intensity
    horiz = {}
    vert = {}
    
    # traverse pixels in a direction
    # if intensity greater than threshold, vote for value and neighborhood
    THRES_BLACK = 70
    
    NEIGH_SIZE = 5
    for x in range(width):
        for y in range(height):
            if prewitt_pixels[x, y] < THRES_BLACK:
                # pixel only votes if direct neighborhood is dark
                # check if average intensity of direct neighborhood over threshold
                average_intensity = 0
                num_pixels = 0
                
                for x_offset in range (-1, 1):
                    neigh_x = x + x_offset
                    # if within image, factor into average
                    if neigh_x < 0 or neigh_x >= width:
                        continue
                    for y_offset in range (-1, 1):
                        neigh_y = y + y_offset
                        # if within image, factor into average
                        if neigh_y < 0 or neigh_y >= height:
                            continue
                            
                        average_intensity += prewitt_pixels[x + x_offset, y+y_offset]
                        num_pixels += 1
                
                average_intensity = average_intensity / num_pixels
                if average_intensity >= THRES_BLACK:
                    continue
                    
                # if neighborhood dark enough
                # pixel votes for everything in neighborhood
                
                # horizontal: x voting
                for x_offset in range (-1 * NEIGH_SIZE, NEIGH_SIZE):
                    neigh_x = x + x_offset
                    
                    # if within image, increment
                    if neigh_x < 0 or neigh_x >= width:
                        continue
                    if neigh_x not in horiz:
                        horiz[neigh_x] = 1
                    else:
                        horiz[neigh_x] += 1
                
                # vertical: y voting
                for y_offset in range (-1 * NEIGH_SIZE, NEIGH_SIZE):
                    neigh_y = y + y_offset
                    
                    # if within image, increment
                    if neigh_y < 0 or neigh_y >= height:
                        continue
                    if neigh_y not in vert:
                        vert[neigh_y] = 1
                    else:
                        vert[neigh_y] += 1
            
    # look in appropriate dictionaries for max/min x/y values
    horiz = sorted(horiz.iteritems(), key=lambda (k,v): (v,k))
    vert = sorted(vert.iteritems(), key=lambda (k,v): (v,k))
    
    x1 = horiz[len(horiz)-1][0]
    x2 = x1
    y1 = vert[len(vert)-1][0]
    y2 = y1
    
    FRACTION = .2
    MIN_DIST_X = FRACTION * width
    x_index = len(horiz)-1
    while abs(x2 - x1) < MIN_DIST_X:
        x2 = horiz[x_index][0]
        x_index -= 1
    
    MIN_DIST_Y = FRACTION * height
    y_index = len(vert)-1
    while abs(y2 - y1) < MIN_DIST_Y:
        y2 = vert[y_index][0]
        y_index -=1
    
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)
    
    if DRAW:
        draw = ImageDraw.Draw(both)
        draw.line((x1, 0, x1, height), fill=128)
        draw.line((x2, 0, x2, height), fill=128)
        draw.line((0, y1, width, y1), fill=128)
        draw.line((0, y2, width, y2), fill=128)
        del draw
    ImageShow.show(both, 'with points')
    both.save('./images/intermediate/' + pic_name + '_getpicture_precrop.jpg');
    
    # crop image
    BUFFER = 5
    min_x = max(0, min_x - BUFFER)
    max_x = min(width - 1, max_x + BUFFER)
    min_y = max(0, min_y - BUFFER)
    max_y = min(height - 1, max_y + BUFFER)
    image = image.crop([min_x, min_y, max_x, max_y]);
    
    image.save('./images/intermediate/' + pic_name + '_getpicture_cropped.jpg');
    
    return image # picture


if __name__=='__main__':
    result = picture('webcam', './images/webcam.jpg')
    ImageShow.show(result, "window title")



