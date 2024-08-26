import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img=cv.imread('Thor.jpg')
kernel=np.ones((5,5),np.float64)/25
dst=cv.filter2D(img,-1,kernel)
gblur=cv.GaussianBlur(img,(7,7),0)
mblur=cv.medianBlur(img,3)
bilat=cv.bilateralFilter(img,-1,7,30,30)
box=cv.boxFilter(img,0,(7,7),(-1,-1))
l=[img,dst,gblur,bilat,mblur,box]
t=["Original","2D Convolution","GaussianBlur","BilateralFilter","MedianBlur","BoxFilter"]
for i in range(6):
    plt.subplot(3,3,i+1)
    plt.imshow(l[i],'gray')
    plt.title(t[i])
    plt.xticks([]),plt.yticks([])
plt.show()