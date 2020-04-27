 
import numpy as np
import cv2
import time
import sys
import subprocess
import os

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

    outname = "/out/mojo.avi"
    codec = cv2.VideoWriter_fourcc(*'MPEG')
    output = cv2.VideoWriter(outname, cv2.CAP_FFMPEG, codec, meanfps, (width,height))

    wantframes=10

    while(wantframes>0):
        hasframes, frame = cap.read()
        if(not hasframes):
            continue
        elif(np.shape(frame) == ()):
            continue
        elif(np.sum(frame) == 0):
            continue
        else: 
            wantframes=wantframes-1
            output.write(frame)

    output.release()

if __name__ == '__main__':
    main()



