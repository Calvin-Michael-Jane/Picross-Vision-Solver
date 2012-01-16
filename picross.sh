#!/bin/bash
./testopencv/webcam/webcam &
echo "GET READY AND PRESS [ENTER]"
read userinput
echo -ne "3..."
sleep 0.5 
echo -ne "2..."
sleep 0.5
echo -ne "1..."
sleep 0.5
./imagesnap -> ./images/snapshot.jpg
afplay /Applications/Utilities/Grab.app/Contents/Resources/OpenShutter.snd
afplay /Applications/Utilities/Grab.app/Contents/Resources/CloseShutter.snd
echo "GOT IT"
kill $!
python2.7 picross.py


