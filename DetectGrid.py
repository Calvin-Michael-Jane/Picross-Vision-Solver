#!/usr/bin/python

# Return the picture for use in the Picross Solver
# May return a constant picture or a web camera image
import Image, ImageDraw
import ImageFilter
import ImageOps, ImageShow
#import heapq
import Representations
import prewitt
from math import floor

global_board_size = 10

def detect(picture):
    grid = [(4,4),(10,4),(10,10),(4,10)] # grid corners
    cell_length = 2
    gr = Representations.GridRep(grid, cell_length)
    return gr # grid representation


def detect_lines(picture, name):
    if picture.mode != 'L' : picture = picture.convert('L')
    pixels = list(picture.getdata())
    width, height = picture.size
    (both, hor_filt, vert_filt) = prewitt.prewitt(pixels, width, height)
    
    picture.save("./images/original.jpg")

    v = "vertical"
    h = "horizontal"
    (saved, xcoords) = detect_hv_lines(hor_filt,h)
    (savedy, ycoords) = detect_hv_lines(vert_filt,v)

    paint_lines(hor_filt,saved,h).save("./images/saveda.jpg")
    paint_lines(vert_filt,savedy,v).save("./images/savedv.jpg")


    # we'll trust the max coordinates as those are near the edge of the image
    # and are unlikely to be mistaken compared to the min coordinates
    max_x = max(xcoords)
    max_y = max(ycoords)
    min_x = min(xcoords)
    min_y = min(ycoords)

    projected_avg_x = (max_x-min_x)/global_board_size
    projected_avg_y = (max_y-min_y)/global_board_size

    avg_x = vote_avg_diff(xcoords)
    avg_y = vote_avg_diff(ycoords)
    #avg = (avg_x+avg_y)/2
    print "avg x diff: ", projected_avg_x
    print "avg y diff: ", projected_avg_y
    print "voted x df: ", avg_x
    print "voted y df: ", avg_y


    # get an evenly spaced set of lines
    xcoords = extrapolate_coords(max_x, projected_avg_x)
    ycoords = extrapolate_coords(max_y, projected_avg_y)
    #xcoords = extrapolate_coords(max_x, avg_x)
    #ycoords = extrapolate_coords(max_y, avg_y)


    paintedh = paint_lines(hor_filt,xcoords,h)
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
    draw.rectangle(grid_coords,outline=128)
    del draw
    combined.save("./images/painted_lines_both_"+name+".jpg")
    ImageShow.show(combined,"blah")
    

    # return a Grid Representation of this solution
    cell_width = projected_avg_x
    cell_height = projected_avg_y
    gr = Representations.GridRep(grid_coords, ycoords, xcoords, cell_height, cell_width)
    return gr

def extrapolate_coords(start, avg):
    new_coords = []
    for i in xrange(global_board_size+1):
        new_val = floor(start-(i*avg))
        if new_val < 0 : continue
        new_coords.append(floor(start-(i*avg)))
    return new_coords

def vote_avg_diff(coords):
    coords.sort()
    votes = {}
    prev_coord = -1
    min_range = -1
    max_range = 1
    for coord in coords:
        diff = coord - prev_coord
        if prev_coord >= 0:
            for x in range(min_range,max_range+1):
                if (x+diff) not in votes : votes[x+diff]=0
                votes[x+diff]+=1
        prev_coord = coord
    return max(votes)

def get_avg_diff(coords):
    coords.sort()
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
    threshold = 130
    window_size = 15
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
                for line_i in range(0,longest_line,window_size):
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

    saved_coords = list(coords)

    num_removed = 1
    while num_removed > 0:
        print "coords: ", coords
        (coords,num_removed) = clean_lines(coords)
        print "num removed: ", num_removed
        
    return (saved_coords,coords)


# get rid of multiple lines corresponding to the same position
# and remove lines that do not seem to be at the equal spacing
# found within the actual grid
def clean_lines(coords):
    min_space = 4

    coords.sort()
    prev_coord = coords[0]
    cleaned_coords = []
    for coord in coords:
        space = coord - prev_coord
        print "spaces: ", space
        if space >= min_space:
            cleaned_coords.append(prev_coord)
        prev_coord = coord

    # finish the cleaning of nothing is left to be done
    if not cleaned_coords:
        return (coords,0)

    # take care of final case
    if prev_coord > (max(cleaned_coords)+min_space):
        cleaned_coords.append(prev_coord)


    # now get rid of extraneous lines that are outside the grid
    # and get the average grid width
    avg_diff = get_avg_diff(cleaned_coords)
    max_tolerated = avg_diff * 2
    min_tolerated = avg_diff * 0.3
    print 'avg_diff: ', avg_diff
    
    num_removed = 0
    prev_coord = -1
    for coord in cleaned_coords:
        diff = coord - prev_coord
        print '{0} to {1} has diff: {2}'.format(prev_coord,coord,diff)
        if (prev_coord >= 0) and (diff > max_tolerated):
            print "{0}--diff removed; {1}--coord removed".format(diff,prev_coord)
            cleaned_coords.remove(prev_coord)
            num_removed+=1
        elif (prev_coord >=0) and (diff < min_tolerated):
            print "{0}--diff split; {1}--coord removed".format(diff,prev_coord)
            cleaned_coords.remove(prev_coord)
            avg_point = floor((diff / 2) + prev_coord)
            cleaned_coords.insert(0,avg_point)
            print "avg point: ", avg_point, " added"
            num_removed+=1
        prev_coord = coord

    return (cleaned_coords,num_removed)

# visualize the resulting lines on the image post filter
def paint_lines(picture, coords, direction):
    width, height = picture.size
    outimg = Image.new('L', (width, height))
    outpixels = outimg.load()
    v="vertical"
    h="horizontal"
    print "current coords: ", coords
    for coord in coords:
        if direction==v:
            max_line = height
        elif direction==h:
            max_line = width
        for i in xrange(max_line):
            if direction==v:
                outpixels[coord,i] = 255
            elif direction==h:
                #print "fail i: {0}\tfail coord: {1}".format(i, coord)
                outpixels[i,coord] = 255
    print "coords: ", coords
    return Image.blend(ImageOps.invert(outimg).convert("RGB"),picture.convert("RGB"),0.2)


# testing main
if __name__=='__main__':
    """    test_pic = './images/red_cropped.jpg'
    image = Image.open(test_pic)
    (xcoords, ycoords) = detect_lines(image,"red")
    print "Red box sizes: (x then y)"
    print get_avg_diff(xcoords)
    print get_avg_diff(ycoords)
    """
    test_pic = './images/blue.jpg'
    image = Image.open(test_pic)
    (xcoords,ycoords) = detect_lines(image,"test")
    print "Blue box sizes: (x then y)"
    print get_avg_diff(xcoords)
    print get_avg_diff(ycoords)

    #print 'grid: ',
    #print puzzlegrid.grid
    #print 'cell length: ',
    #print puzzlegrid.cell_length



