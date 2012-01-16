#!/bin/bash
./testopencv/webcam/webcam &
echo "GET READY AND PRESS [ENTER]"
read userinput
echo -ne "3..."
sleep 1
echo -ne "2..."
sleep 1
echo -ne "1..."
sleep 1
./imagesnap -> snapshot.jpg
afplay /Applications/Utilities/Grab.app/Contents/Resources/OpenShutter.snd
afplay /Applications/Utilities/Grab.app/Contents/Resources/CloseShutter.snd
echo "GOT IT"
kill $!
python2.7 ReadPic.py
open snapshot_e.jpg


