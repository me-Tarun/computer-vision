import cv2 
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('Korg.jpg',0)
clahe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
hist=cv2.calcHist([img],[0],None,[250],[0,255])
eq=cv2.equalizeHist(img)
p1=cv2.calcHist([eq],[0],None,[250],[0,255])
cl=cv2.equalizeHist(img)
p2=cv2.calcHist([cl],[0],None,[250],[0,255])
l=[img,eq,cl]
j=0
plots=[hist,p1,p2]
for i in range(0,9,3):
    plt.subplot(3,3,i+1)
    plt.imshow(l[j],'gray')
    plt.xticks([]),plt.yticks([])
    plt.subplot(3,3,i+2)
    plt.plot(plots[j])
    j+=1
plt.show()