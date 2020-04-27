 
import numpy as np
import cv2
import time
import sys
import subprocess

def main():

    name = "/out/mojo.avi"
    width = height = meanfps = 100
    codec = cv2.VideoWriter_fourcc(*'MPEG')
    output = cv2.VideoWriter(name, cv2.CAP_FFMPEG, codec, meanfps, (width,height))
    output.release()

if __name__ == '__main__':
    main()



