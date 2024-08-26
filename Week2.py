import cv2 as cv
import numpy as np
img=cv.imread("Thor.jpg")
sum=cv.sumElems(img)
avg=cv.mean(img)
mean,std=cv.meanStdDev(img)
#min_val,max_val,min_loc,max_loc=cv.minMaxLoc(img)
print(f" SUM: {sum}")
print(f" Average: {avg}")
print(f" Standard Deviation: {std}")
#print(f" Minimum: {min_loc}")
#print(f" Maximum: {max_loc}")