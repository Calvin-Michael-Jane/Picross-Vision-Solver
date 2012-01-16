#!/usr/bin/python

# Return the picture for use in the Picross Solver
# May return a constant picture or a web camera image
import Image
import DetectGrid

def find_numbers(puzzlegrid, skewless_picture):
    positions = [];
    
    # traverse grid, determine min/max x and y coords
    min_x = max_x = puzzlegrid.grid[0][0]
    min_y = max_y = puzzlegrid.grid[0][1]
    
    for i in range(1, 4):
        if puzzlegrid.grid[i][0] < min_x:
            min_x = puzzlegrid.grid[i][0]
        elif puzzlegrid.grid[i][0] > max_x:
            max_x = puzzlegrid.grid[i][0]
        if puzzlegrid.grid[i][1] < min_y:
            min_y = puzzlegrid.grid[i][1]
        elif puzzlegrid.grid[i][1] > max_y:
            max_y = puzzlegrid.grid[i][1]
    
    #print min_x
    #print max_x
    #print min_y
    #print max_y
    
    # convert image to grayscale array
    grayscale_picture = skewless_picture.convert("L")
    pixels = grayscale_picture.load()
    
    # calculate average change in color per cell
    # compare to threshold, if greater, has number
    thres = 10 #??
    left_num_x = int(min_x / puzzlegrid.cell_length)
    left_num_y = int((max_y - min_y) / puzzlegrid.cell_length)
    
    #print "left # cells: "
    #print left_num_x
    #print left_num_y
    
    # left
    for i in range(left_num_x):
        for j in range(left_num_y):
            # for each cell, traverse pixels
            
            # calculate average
            average = 0
            for k in range(puzzlegrid.cell_length):
                for l in range(puzzlegrid.cell_length):
                    x = i * puzzlegrid.cell_length + k
                    y = min_y + j * puzzlegrid.cell_length + l
                    average += pixels[x, y] #??
            average /= pow(puzzlegrid.cell_length, 2)
            
            # calculate variance
            variance = 0
            for k in range(puzzlegrid.cell_length):
                for l in range(puzzlegrid.cell_length):
                    x = i * puzzlegrid.cell_length + k
                    y = min_y + j * puzzlegrid.cell_length + l
                    variance += pow(pixels[x, y] - average, 2) #??
            variance /= pow(puzzlegrid.cell_length, 2)
            
            #print "avg: "
            #print average
            #print "var: "
            #print variance
            
            # has number, save cell top-left corner in positions
            if variance > thres:
                x = i * puzzlegrid.cell_length 
                y = min_y + j * puzzlegrid.cell_length
                positions.append((x, y))
                
    # top
    top_num_x = int((max_x - min_x) / puzzlegrid.cell_length)
    top_num_y = int(min_y / puzzlegrid.cell_length)
    
    for i in range(top_num_x):
        for j in range(top_num_y):
            # for each cell, traverse pixels
            
            # calculate average
            average = 0
            for k in range(puzzlegrid.cell_length):
                for l in range(puzzlegrid.cell_length):
                    x = i * puzzlegrid.cell_length + k
                    y = min_y + j * puzzlegrid.cell_length + l
                    average += pixels[x, y] #??
            average /= pow(puzzlegrid.cell_length, 2)
            
            # calculate variance
            variance = 0
            for k in range(puzzlegrid.cell_length):
                for l in range(puzzlegrid.cell_length):
                    x = min_x + i * puzzlegrid.cell_length + k
                    y = j * puzzlegrid.cell_length + l
                    variance += pow(pixels[x, y] - average, 2) #??
            variance /= pow(puzzlegrid.cell_length, 2)
            
            #print "avg: "
            #print average
            #print "var: "
            #print variance
            
            # has number, save cell top-left corner in positions
            if variance > thres:
                x = min_x + i * puzzlegrid.cell_length 
                y = j * puzzlegrid.cell_length
                positions.append((x, y))

    return positions # number positions


# testing main
if __name__=='__main__':
    test_pic = './images/blue_9.jpg'
    image = Image.open(test_pic)
    puzzlegrid = DetectGrid.detect(image)
    nums = find_numbers(puzzlegrid, image)
    print nums


