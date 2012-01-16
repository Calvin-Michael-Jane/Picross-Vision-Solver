
import Image
import ImageShow
import Representations
import NeuralNetwork

puzzle_size = 5

def ocr(num_pos, picture, puzzlegrid):
    # set up neural network
    net = NeuralNetwork.NeuralNetwork('data/ocr.train', 100)
    
    # predict each number
    for x in num_pos:
        digit_image = picture.crop([int(x[0]), int(x[1]), int(x[0]) + puzzlegrid.cell_width, int(x[1]) + puzzlegrid.cell_height]) 
        digit_image = digit_image.convert("L")
        digit_image = digit_image.resize([14, 14])
        digit_pixels = digit_image.load()
        width, height = digit_image.size
        
        # clamp values to 0, 255
        testsample = []
        for x in range(width):
            for y in range(height):
                if digit_pixels[x, y] < 127:
                    digit_pixels[x, y] = 0
                else:
                    digit_pixels[x, y] = 255;
                testsample.append(float(digit_pixels[x, y])/255.0)
        digit = net.predict(testsample)
        print digit
        digit_image.show(str(digit))
        
    top = [[0]*puzzle_size for x in xrange(puzzle_size)] #2D array
    side = [[0]*puzzle_size for x in xrange(puzzle_size)]
    pr = Representations.PuzzleRep(top, side) # consists of side and top 2D arrays
    return pr # puzzle representation

# i write neural network now l0l

# testing main
if __name__=='__main__':
    test_pic = './images/testpicture.jpg'
    image = Image.open(test_pic)
    number_positions = [(0,0), (1,1)]
    puzzle = ocr(number_positions, image)
    print 'top: ',
    print puzzle.top
    print 'side: ',
    print puzzle.side


