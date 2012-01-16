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

pic_name = 'blue'
test_pic = './images/' + pic_name + '.jpg'

# main
if __name__=='__main__':
    #original_picture = GetPicture.picture(test_pic)
    original_picture = Image.open(test_pic)
    skewless_picture = AntiSkew.fix_skew(original_picture)
    puzzlegrid = DetectGrid.detect_lines(skewless_picture,"test")
    number_positions = FindNumbers.find_numbers(puzzlegrid, skewless_picture, pic_name)
    puzzle = OCRNumbers.ocr(number_positions, skewless_picture, puzzlegrid)
    solution = PicrossSolver.solve(puzzle)
    DisplayPuzzle.visualize(solution)


