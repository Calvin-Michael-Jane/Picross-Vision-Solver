#!/bin/bash
# script to run all of the testing mains
# for the classes used by picross.py
echo 'running main picross solver'
python2.7 picross.py
echo 'running GetPicture'
python2.7 GetPicture.py
echo 'running AntiSkew'
python2.7 AntiSkew.py
echo 'running DetectGrid'
python2.7 DetectGrid.py
echo 'running FindNumbers'
python2.7 FindNumbers.py
#echo 'running OCRNumbers'
#python2.7 OCRNumbers.py
#echo 'running PicrossSolver'
#python2.7 PicrossSolver.py
#echo 'running DisplayPuzzle'
#python2.7 DisplayPuzzle.py
