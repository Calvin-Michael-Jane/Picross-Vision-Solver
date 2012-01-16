#!/usr/bin/python

# Return the picture for use in the Picross Solver
# May return a constant picture or a web camera image
import Image
import DetectGrid
import ImageShow
import ImageDraw

TRAIN = False # produces images for training if true
DRAW = False

def find_numbers(puzzlegrid, skewless_picture, pic_name):
    positions = [];
    
    width, height = skewless_picture.size
    print "image size: ", width, height
    
    # traverse grid, determine min/max x and y coords
    min_x = int(puzzlegrid.grid[0][0])
    max_x = int(puzzlegrid.grid[1][0])
    min_y = int(puzzlegrid.grid[0][1])
    max_y = int(puzzlegrid.grid[1][1])
    
    print "min x, max x: ", min_x,  max_x
    print "min_y, max_y: ", min_y,  max_y
    
    # convert image to grayscale array
    grayscale_picture = skewless_picture.convert("L")
    pixels = grayscale_picture.load()
    
    # calculate average change in color per cell
    # compare to threshold, if greater, has number
    THRES = 2000 #??
    
    #draw = ImageDraw.Draw(skewless_picture)
    #for y in range(min_y, 0, -puzzlegrid.cell_height):  
    #    draw.line((min_x, y, max_x, y), fill = 128)
    #for x in range(min_x, 0, -puzzlegrid.cell_width):
    #    draw.line((x, min_y, x, max_y), fill = 128)
    
    # top
    for x in puzzlegrid.x_coords:
        if x == max_x:
            continue
            
        for y in range(min_y - puzzlegrid.cell_height, 0, -puzzlegrid.cell_height):  
            # calculate average
            average = 0
            for k in range(puzzlegrid.cell_width):
                for l in range(puzzlegrid.cell_height):
                    curr_x = x + k
                    curr_y = y + l
                    average += pixels[curr_x, curr_y] #??
            average /= (puzzlegrid.cell_width * puzzlegrid.cell_height)
            
            # calculate variance
            variance = 0
            for k in range(puzzlegrid.cell_width):
                for l in range(puzzlegrid.cell_height):
                    curr_x = x + k
                    curr_y = y + l
                    variance += pow(pixels[curr_x, curr_y] - average, 2) #??
            variance /= (puzzlegrid.cell_width * puzzlegrid.cell_height)
            
            # has number, save cell top-left corner in positions
            if variance > THRES:
                positions.append((x, y))
            else:
                break
    # left
    for y in puzzlegrid.y_coords:
        if y == max_y:
            continue
            
        for x in range(min_x - puzzlegrid.cell_width, 0, -puzzlegrid.cell_width):
            # calculate average
            average = 0
            for k in range(puzzlegrid.cell_width):
                for l in range(puzzlegrid.cell_height):
                    curr_x = x + k
                    curr_y = y + l
                    average += pixels[curr_x, curr_y] #??
            average /= (puzzlegrid.cell_width * puzzlegrid.cell_height)
            
            # calculate variance
            variance = 0
            for k in range(puzzlegrid.cell_width):
                for l in range(puzzlegrid.cell_height):
                    curr_x = x + k
                    curr_y = y + l
                    variance += pow(pixels[curr_x, curr_y] - average, 2) #??
            variance /= (puzzlegrid.cell_width * puzzlegrid.cell_height)
            
            # has number, save cell top-left corner in positions
            if variance > THRES:
                positions.append((x, y))
            else:
                break
                
    if DRAW:
        draw = ImageDraw.Draw(skewless_picture)
        BOXSIZE = 3
        for point in positions:
            ptx = point[0]
            pty = point[1]  
            draw.rectangle([ptx-BOXSIZE, pty-BOXSIZE, ptx+BOXSIZE, pty+BOXSIZE], fill=128)
        del draw
        ImageShow.show(skewless_picture, 'with points')
    
    # save training images
    if TRAIN:
        for point in positions:
            ptx = int(point[0])
            pty = int(point[1])
            picture = skewless_picture.crop([ptx, pty, ptx + puzzlegrid.cell_width, pty + puzzlegrid.cell_height]);
            picture.save("./images/train/{0}_{1}_{2}.jpg".format(pic_name, ptx, pty))

    return positions # number positions


# testing main
if __name__=='__main__':
    test_pic = './images/blue_9.jpg'
    image = Image.open(test_pic)
    puzzlegrid = DetectGrid.detect(image)
    nums = find_numbers(puzzlegrid, image)
    print nums


