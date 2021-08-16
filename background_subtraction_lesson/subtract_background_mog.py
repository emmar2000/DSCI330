import numpy as np
import cv2 as cv
cap = cv.VideoCapture('https://file-examples-com.github.io/uploads/2018/04/file_example_AVI_480_750kB.avi')
fgbg = cv.bgsegm.createBackgroundSubtractorMOG()
count = 10
while(1):
    ret, frame = cap.read()
    if not ret:
        break
    fgmask = fgbg.apply(frame)
    #cv.imshow('frame',fgmask)
    cv.imwrite(f"frame_{count}.png", fgmask)
    count += 1
    print(count)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()