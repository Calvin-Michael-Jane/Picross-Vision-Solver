
import Image
import ImageShow
import Representations
import NeuralNetwork

puzzle_size = 5

def ocr(num_pos, picture, puzzlegrid):
    
    top = []
    side = []
    
    # set up neural network
    net = NeuralNetwork.NeuralNetwork('data/ocr.train', 100)
    
    # predict each number
    for a in num_pos.top:
        pred = []
        for x in a:
            prediction = ocr_digit(x, picture, puzzlegrid, net)
            pred.append(prediction)
        top.append(pred)
    
    for a in num_pos.side:
           pred = []
           for x in a:
               prediction = ocr_digit(x, picture, puzzlegrid, net)
               pred.append(prediction)
           side.append(pred)
    
    print top
    print side
    
    pr = Representations.PuzzleRep(top, side) # consists of side and top 2D arrays
    return pr # puzzle representation

def ocr_digit(coordinate, picture, puzzlegrid, net):
    digit_image = picture.crop([int(coordinate[0]), int(coordinate[1]), int(coordinate[0]) + puzzlegrid.cell_width, int(coordinate[1]) + puzzlegrid.cell_height]) 
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
    return net.predict(testsample)

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


