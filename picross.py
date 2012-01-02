#!/usr/bin/python

# Main skeleton for Picross Solver
# Indentation is set to 4 spaces, no hard tabs

import GetPicture
import AntiSkew
import DetectPuzzle
import FindNumbers
import OCRNumbers
import PicrossSolver
import DisplayPuzzle

# main
if __name__=='__main__':
    original_picture = GetPicture.picture()
    skewless_picture = AntiSkew.fix_skew(original_picture)
    puzzlegrid = DetectPuzzle.detect(skewless_picture)
    number_positions = FindNumbers.find_numbers(puzzlegrid, skewless_picture)
    puzzle = OCRNumbers.ocr(number_positions, skewless_picture)
    solution = PicrossSolver.solve(puzzle)
    DisplayPuzzle.visualize(solution)


