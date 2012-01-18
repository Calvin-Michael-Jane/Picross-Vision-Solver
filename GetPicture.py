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
    pixels = image.load();
    
    width, height = image.size
    
    center = (width/2, height/2)
    
    # center intensity should be in DS screen and therefore above some threshold
    cent_x = center[0]
    cent_y = center[1]
    screen_intensity = (pixels[center] + pixels[cent_x-1, cent_y-1] + pixels[cent_x-1, cent_y] + pixels[cent_x-1, cent_y+1] + pixels[cent_x, cent_y-1] + pixels[cent_x, cent_y+1] + pixels[cent_x+1, cent_y-1] + pixels[cent_x+1, cent_y] + pixels[cent_x+1, cent_y+1]) / 9.
    X_INC = width / 100
    Y_INC = height / 100
    THRES_DIFF = 40
    NEIGH_SIZE = 5
    
    # get max x of screen border
    prev_intensity = screen_intensity
    potential_border = width
    for x in range(center[0] + X_INC, width, X_INC):
        # get average of neighborhood
        average_intensity = 0
        num_pixels = 0
                
        for x_offset in range(-1 * NEIGH_SIZE, 1 * NEIGH_SIZE):
            neigh_x = x + x_offset
            # if within image, factor into average
            if neigh_x < 0 or neigh_x >= width:
                continue
            for y_offset in range(-1 * NEIGH_SIZE, 1 * NEIGH_SIZE):
                neigh_y = cent_y + y_offset
                # if within image, factor into average
                if neigh_y < 0 or neigh_y >= height:
                    continue
                            
                average_intensity += pixels[neigh_x, neigh_y]
                num_pixels += 1
                
        average_intensity = average_intensity / num_pixels
        
        if abs(average_intensity - prev_intensity) > THRES_DIFF:
            if potential_border < width:
                break
            potential_border = x
        else:
            potential_border = width
            prev_intensity = average_intensity
    max_x = potential_border
    print max_x
    
    # get min x of screen border
    prev_intensity = screen_intensity
    potential_border = 0
    for x in range(center[0] - X_INC, 0, -1 * X_INC):
        # get average of neighborhood
        average_intensity = 0
        num_pixels = 0
                
        for x_offset in range(-1 * NEIGH_SIZE, 1 * NEIGH_SIZE):
            neigh_x = x + x_offset
            # if within image, factor into average
            if neigh_x < 0 or neigh_x >= width:
                continue
            for y_offset in range(-1 * NEIGH_SIZE, 1 * NEIGH_SIZE):
                neigh_y = cent_y + y_offset
                # if within image, factor into average
                if neigh_y < 0 or neigh_y >= height:
                    continue
                            
                average_intensity += pixels[neigh_x, neigh_y]
                num_pixels += 1
                
        average_intensity = average_intensity / num_pixels
        
        if abs(average_intensity - prev_intensity) > THRES_DIFF:
            if potential_border > 0:
                break
            potential_border = x
        else:
            potential_border = 0
            prev_intensity = average_intensity
    min_x = potential_border
    print min_x
    
    # get max y of screen border
    prev_intensity = screen_intensity
    potential_border = height
    for y in range(center[1] + Y_INC, height, Y_INC):
        # get average of neighborhood
        average_intensity = 0
        num_pixels = 0
                
        for x_offset in range(-1 * NEIGH_SIZE, 1 * NEIGH_SIZE):
            neigh_x = cent_x + x_offset
            # if within image, factor into average
            if neigh_x < 0 or neigh_x >= width:
                continue
            for y_offset in range(-1 * NEIGH_SIZE, 1 * NEIGH_SIZE):
                neigh_y = y + y_offset
                # if within image, factor into average
                if neigh_y < 0 or neigh_y >= height:
                    continue
                            
                average_intensity += pixels[neigh_x, neigh_y]
                num_pixels += 1
                
        average_intensity = average_intensity / num_pixels
        
        if abs(average_intensity - prev_intensity) > THRES_DIFF:
            if potential_border < height:
                break
            potential_border = y
        else:
            potential_border = height
            prev_intensity = average_intensity
    max_y = potential_border
    print max_y
    
    # get min y of screen border
    prev_intensity = screen_intensity
    potential_border = 0
    for y in range(center[1] - Y_INC, 0, -1 * Y_INC):
        # get average of neighborhood
        average_intensity = 0
        num_pixels = 0
                
        for x_offset in range(-1 * NEIGH_SIZE, 1 * NEIGH_SIZE):
            neigh_x = cent_x + x_offset
            # if within image, factor into average
            if neigh_x < 0 or neigh_x >= width:
                continue
            for y_offset in range(-1 * NEIGH_SIZE, 1 * NEIGH_SIZE):
                neigh_y = y + y_offset
                # if within image, factor into average
                if neigh_y < 0 or neigh_y >= height:
                    continue
                            
                average_intensity += pixels[neigh_x, neigh_y]
                num_pixels += 1
                
        average_intensity = average_intensity / num_pixels
        
        if abs(average_intensity - prev_intensity) > THRES_DIFF:
            if potential_border > 0:
                break
            potential_border = y
        else:
            potential_border = 0
            prev_intensity = average_intensity
    min_y = potential_border
    print min_y
    
    """pixels = list(image.getdata())
    
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
    max_y = max(y1, y2)"""
    
    if DRAW:
        draw = ImageDraw.Draw(image)
        draw.line((min_x, 0, min_x, height), fill=128)
        draw.line((max_x, 0, max_x, height), fill=128)
        draw.line((0, min_y, width, min_y), fill=128)
        draw.line((0, max_y, width, max_y), fill=128)
        del draw
    ImageShow.show(image, 'with points')
    image.save('./images/intermediate/' + pic_name + '_getpicture_precrop.jpg')
    
    # crop image
    BUFFER = 5
    min_x = max(0, min_x - BUFFER)
    max_x = min(width - 1, max_x + BUFFER)
    min_y = max(0, min_y - BUFFER)
    max_y = min(height - 1, max_y + BUFFER)
    image = image.crop([min_x, min_y, max_x, max_y]);
    
    image.save('./images/intermediate/' + pic_name + '_getpicture_cropped.jpg')
    
    return image # picture


if __name__=='__main__':
    result = picture('webcam', './images/webcam.jpg')
    ImageShow.show(result, "window title")



