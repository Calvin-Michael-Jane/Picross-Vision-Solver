#!/usr/bin/python

# Return the picture for use in the Picross Solver
# May return a constant picture or a web camera image
import Image
import Representations
import ImageShow

puzzle_size = 5
SIDE_LENGTH = 20

def visualize(solution):
    print solution.solution
    image = Image.new('L', (len(solution.solution[0]) * SIDE_LENGTH, len(solution.solution) * SIDE_LENGTH))
    pixels = image.load()
    
    for x in range(len(solution.solution[0])):
        for y in range(len(solution.solution)):
            for i in range(SIDE_LENGTH):
                for j in range(SIDE_LENGTH):
                    curr_x = x * SIDE_LENGTH + i 
                    curr_y = y * SIDE_LENGTH + j
                    if solution.solution[y][x] == 0:
                        pixels[curr_x, curr_y] = 255
                    else:
                        pixels[curr_x, curr_y] = 0
    
    ImageShow.show(image, 'solution')
    image.save('fakesolution.jpg')
    


# testing main
if __name__=='__main__':
    test_pic = './images/testpicture.jpg'
    image = Image.open(test_pic)
    answer = [[0, 1, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 0, 1, 1, 0, 0]]
    #[[0]*puzzle_size for x in xrange(puzzle_size)]
    solution = Representations.SolutionRep(answer)
    visualize(solution)

