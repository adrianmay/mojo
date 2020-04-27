 
import numpy as np
import cv2
import time
import sys
import subprocess
import os

YOUNG=-1
IDLE=0
CURIOUS=1
ALARMED=2
ANNOYED=4

state = YOUNG
fnum = 0

def main():

    cam = os.environ['CAM']
    cap = cv2.VideoCapture(cam, cv2.CAP_ANY)
    if not cap.isOpened():
        raise IOError("Cannot open the selected video/camera")
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print ("Video Height {0} Width {1}".format(height, width))

    tframe0 = time.time()
    tframe1 = tframe0
    fps = 0
    meanfps = 1.0 # guess this for your cam

    wantframes=30
    fnum=1

    while(wantframes>fnum):
        hasframes, frame = cap.read()
        if(not hasframes):
            continue
        elif(np.shape(frame) == ()):
            continue
        elif(np.sum(frame) == 0):
            continue

        fnum=fnum+1
        cv2.imwrite("/out/still_{0}.jpg".format(fnum), frame)
        # Then stitch them together with ffmpeg -framerate 1 -start_number 1 -i still_%d.jpg -vcodec libx264 -b 800k test.avi
        # if( (cv2.waitKey(1) & 0xFF) == ord('q') ):
        #    break

if __name__ == '__main__':
    main()



