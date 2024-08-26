import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread("L.jpg")
img1=cv2.imread("L.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,50,150)
lines=cv2.HoughLinesP(edges,1,np.pi/180,100,100,10)
for line in lines:
    x1,y1,x2,y2=line[0]
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),6)
tit=["Original","Hough Lines"]
imag=[img1,img]
for i in range(2):
    plt.subplot(2,2,i+1)
    plt.imshow(imag[i],'gray')
    plt.title(tit[i])
    plt.xticks([]),plt.yticks([])
plt.show()