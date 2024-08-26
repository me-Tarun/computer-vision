import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread("C.jpg")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cmy=255-img
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cmyk = cv.cvtColor(img, cv.COLOR_BGR2LAB)
l=[img,gray,cmy,hsv,cmyk]
t=["Original","GrayScale","CMY","HSV","CMYK"]
for i in range(5):
    plt.subplot(2,3,i+1)
    plt.imshow(l[i],'gray')
    plt.title(t[i])
    plt.xticks([]),plt.yticks([])
plt.show()