import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
kernel=np.ones((5,5),np.uint8)
img=cv.imread('MoonKnight.webp',0)
_,img = cv.threshold(img, 150, 255, cv.THRESH_BINARY)
erosion=cv.erode(img,kernel,iterations=3)
dilation=cv.dilate(img,kernel,iterations=3)
opening=cv.morphologyEx(img,cv.MORPH_OPEN,kernel)
closing=cv.morphologyEx(img,cv.MORPH_CLOSE,kernel)
l=[img,erosion,dilation,opening,closing]
t=["Original","Erosion","Dilation","Opening","Closing","Mask"]
for i in range(5):
    plt.subplot(3,3,i+1)
    plt.imshow(l[i],'gray')
    plt.title(t[i])
    plt.xticks([]),plt.yticks([])
plt.show()