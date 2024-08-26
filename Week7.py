import numpy as np
import cv2 
img = cv2.imread("Ear.jpg")
gray = cv2.imread("Ear.jpg",0)
sift=cv2.SIFT_create()
detect = sift.detect(gray,None)
img = cv2.drawKeypoints(gray,detect,img)
cv2.imshow("Image :",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
