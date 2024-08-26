import cv2 as cv
from matplotlib import pyplot as plt
plt.figure(figsize=(10, 10))
img = cv.imread('Peo.jpg')
org=img.copy()
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
canny = cv.Canny(gray, 10, 100)
contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
cv.drawContours(img, contours,-1, (0,0,255),6)
l=[org,img]
t=["Original","Image With Contours"]
for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(l[i])
    plt.title(t[i])
    plt.xticks([]),plt.yticks([])
plt.show()