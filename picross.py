#!/usr/bin/python

# Main skeleton for Picross Solver
# Indentation is set to 4 spaces, no hard tabs

import Image
import GetPicture
import AntiSkew
import DetectGrid
import FindNumbers
import OCRNumbers
import PicrossSolver
import DisplayPuzzle

pic_name = 'snapshot'
test_pic = './images/' + pic_name + '.jpg'

# main
if __name__=='__main__':
<<<<<<< HEAD
    original_picture = GetPicture.picture(pic_name, test_pic)
    #original_picture = Image.open(test_pic)
    skewless_picture = AntiSkew.fix_skew(original_picture)
=======
    #original_picture = GetPicture.picture(pic_name, test_pic)
    original_picture = Image.open(test_pic)
    skewless_picture = AntiSkew.fix_skew(pic_name, original_picture)
>>>>>>> 0d327375a183089fefc8a7d1792d145aa8646a50
    puzzlegrid = DetectGrid.detect_lines(skewless_picture,"test")
    number_positions = FindNumbers.find_numbers(puzzlegrid, skewless_picture, pic_name)
    #puzzle = OCRNumbers.ocr(number_positions, skewless_picture, puzzlegrid)
    #solution = PicrossSolver.solve(puzzle)
    #DisplayPuzzle.visualize(solution)


