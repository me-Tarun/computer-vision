import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img=cv.imread('Sim.png')
kpx=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
kpy=np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
krx=np.array([[1,0],[0,-1]])
kry=np.array([[0,-1],[1,0]])
laplacian=cv.Laplacian(img,cv.CV_64F)
canny=cv.Canny(img, 150, 250)
sobelx=cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
sobely=cv.Sobel(img,cv.CV_64F,0,1,ksize=5)
prewx=cv.filter2D(img,-1,kpx)
prewy=cv.filter2D(img,-1,kpy)
robx=cv.filter2D(img,-1,krx)
roby=cv.filter2D(img,-1,kry)
l=[img,laplacian,canny,sobelx,sobely,prewx,prewy,robx,roby]
t=["Original","Laplacian","Canny","Sobel X","Sobel Y","Prewitt X","Prewitt Y","Robert X","Robert Y"]
for i in range(9):
    plt.subplot(3,3,i+1)
    plt.imshow(l[i],'gray')
    plt.title(t[i])
    plt.xticks([]),plt.yticks([])
plt.show()