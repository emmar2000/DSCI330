from __future__ import print_function
import cv2 as cv
import argparse

parser = argparse.ArgumentParser(description='This program shows how to use background subtraction methods provided by \
                                              OpenCV. You can process both videos and images.')
parser.add_argument('--input', type=str, help='Path to a video or a sequence of image.', default='vtest.avi')
parser.add_argument('--algo', type=str, help='Background subtraction method (KNN, MOG2).', default='MOG2')
args = parser.parse_args()

## [create]
#create Background Subtractor objects
if args.algo == 'MOG2':
    backSub = cv.createBackgroundSubtractorMOG2()
else:
    backSub = cv.createBackgroundSubtractorKNN()
## [create]

## [capture]
capture = cv.VideoCapture(cv.samples.findFileOrKeep(args.input))
if not capture.isOpened:
    print('Unable to open: ' + args.input)
    exit(0)
## [capture]

count = 1

while True:
    ret, frame = capture.read()
    if frame is None:
        break

    

    ## [apply]
    #update the background model
    fgMask = backSub.apply(frame)
    ## [apply]

    

    ## [show]
    #show the current frame and the fg masks
    '''cv.imshow('Frame', frame)
    cv.imshow('FG Mask', fgMask)'''
    #cv.imwrite(f"frame_{count}.png", frame)
    cv.imwrite(f"FG_Mask_{count}.png", fgMask)
    count += 1
    ## [show]
    