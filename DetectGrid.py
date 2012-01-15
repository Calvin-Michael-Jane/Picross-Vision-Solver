#!/usr/bin/python

# Return the picture for use in the Picross Solver
# May return a constant picture or a web camera image
import Image, ImageDraw
import ImageFilter
import ImageOps
import heapq
import Representations
import prewitt
from math import floor

global_board_size = 10

def detect(picture):
    grid = [(0,0),(1,0),(1,1),(0,1)]; # grid corners
    cell_length = 0;
    gr = Representations.GridRep(grid, cell_length)
    return gr # grid representation


def detect_lines(picture, name):
    if picture.mode != 'L' : picture = picture.convert('L')
    pixels = list(picture.getdata())
    width, height = picture.size
    (both, hor_filt, vert_filt) = prewitt.prewitt(pixels, width, height)
    
    v = "vertical"
    h = "horizontal"
    xcoords = detect_hv_lines(hor_filt,h)
    ycoords = detect_hv_lines(vert_filt,v)

    xcoords = heapq.nlargest(global_

    paintedh = paint_lines(hor_filt, xcoords,h)
    paintedh.save("./images/painted_lines_hor_"+name+".jpg")

    paintedv = paint_lines(vert_filt, ycoords,v)
    paintedv.save("./images/painted_lines_vert_"+name+".jpg")

    combined = Image.blend(paintedv, paintedh, 0.5)
    grid_coords = []
    max_x = max(xcoords)
    min_x = min(xcoords)
    max_y = max(ycoords)
    min_y = min(ycoords)
    grid_coords.append((min_y,min_x))
    grid_coords.append((max_y,max_x))

    print "grid_coords:"
    print grid_coords

    draw = ImageDraw.Draw(combined)
    draw.rectangle(grid_coords,fill=128)
    del draw
    combined.save("./images/painted_lines_both_"+name+".jpg")

    return (xcoords,ycoords)
    

def get_avg_diff(coords):
    sum_diffs = 0
    prev_coord = -1
    for coord in coords:
        if prev_coord >= 0:
            sum_diffs += coord - prev_coord
        prev_coord = coord

    num_items = coords.__len__()
    avg_diff = sum_diffs / num_items
    return avg_diff

# direction is direction that the lines are after the filter,
# referring to the lines in out_v
def detect_hv_lines(filtered,direction):

    # Find vertical lines by looking for equally spaced sections
    # with long, connected black sections, determined by votes
    # from a vertical pass where the horizontal bar hits a black
    # spot
    num_passes = 20
    threshold = 120
    window_size = 10
    width,height = filtered.size
    vert_counts = {}
    pic_h = filtered.load()
    v = "vertical"
    h = "horizontal"
    if direction==v:
        sample_max=height
    elif direction==h:
        sample_max=width
    for pass_num in xrange(num_passes):

        # number that is held through the scan
        held = floor(pass_num * (sample_max / num_passes))

        if direction==v:
            scan_max = width
        elif direction==h:
            scan_max = height

        for i in xrange(scan_max): # run across
            if direction==v:
                pic_val = pic_h[i,held]
                longest_line = height-window_size
            elif direction==h:
                pic_val = pic_h[held,i]
                longest_line = width-window_size
            if (pic_val < threshold and (not (i in vert_counts))):
                count = 0
                for line_i in xrange(longest_line):
                    window_val = 0
                    for win_i in xrange(window_size):
                        if direction==v:
                            window_val += pic_h[i,line_i+win_i]
                        elif direction==h:
                            window_val += pic_h[line_i+win_i,i]
                    window_val = window_val / window_size
                    if window_val < threshold:
                        count+=1
                vert_counts[i] = count # count line length
    #print vert_counts

    # remove all of the noise coordinates by taking
    # only lines that have a length at least 20% of the
    # longest line
    max_val = max(vert_counts.values())
    threshold = 0.2 * max_val
    
    coords = []
    for key, value in vert_counts.iteritems():
        if value > threshold:
            coords.append(key)
    coords = clean_lines(coords)
    return coords


# get rid of multiple lines corresponding to the same position
# and remove lines that do not seem to be at the equal spacing
# found within the actual grid
def clean_lines(coords):
    min_space = 4

    coords.sort()
    prev_coord = coords[0]
    cleaned_coords = []
    for coord in coords:
        if not (prev_coord>=(coord-min_space)):
            cleaned_coords.append(prev_coord)
        prev_coord = coord
    # take care of final case
    if prev_coord > (max(cleaned_coords)+min_space):
        cleaned_coords.append(prev_coord)


    # now get rid of extraneous lines that are outside the grid
    # and get the average grid width
    avg_diff = get_avg_diff(cleaned_coords)
    max_tolerated = avg_diff * 3
    min_tolerated = avg_diff * 0.3
    print 'avg_diff: {}'.format(avg_diff)
    
    prev_coord = -1
    for coord in cleaned_coords:
        diff = coord - prev_coord
        print diff
        if (prev_coord >= 0) and ((diff > max_tolerated) or (diff < min_tolerated)):
            cleaned_coords.remove(prev_coord)
        prev_coord = coord

    return cleaned_coords

# visualize the resulting lines on the image post filter
def paint_lines(picture, coords, direction):
    width, height = picture.size
    outimg = Image.new('L', (width, height))
    outpixels = outimg.load()
    v="vertical"
    h="horizontal"
    for coord in coords:
        if direction==v:
            max_line = height
        elif direction==h:
            max_line = width
        for i in xrange(max_line):
            if direction==v:
                outpixels[coord,i] = 255
            elif direction==h:
                outpixels[i,coord] = 255
    print 'coords: {}'.format(coords)
    return Image.blend(ImageOps.invert(outimg).convert("RGB"),picture.convert("RGB"),0.4)


# testing main
if __name__=='__main__':
    test_pic = './red_cropped.jpg'
    image = Image.open(test_pic)
    (xcoords, ycoords) = detect_lines(image,"red")
    print "Red box sizes: (x then y)"
    print get_avg_diff(xcoords)
    print get_avg_diff(ycoords)

    test_pic = './blue.jpg'
    image = Image.open(test_pic)
    (xcoords,ycoords) = detect_lines(image,"blue")
    print "Blue box sizes: (x then y)"
    print get_avg_diff(xcoords)
    print get_avg_diff(ycoords)

    #print 'grid: ',
    #print puzzlegrid.grid
    #print 'cell length: ',
    #print puzzlegrid.cell_length



