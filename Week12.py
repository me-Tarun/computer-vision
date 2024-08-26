import cv2
import numpy as np
from matplotlib import pyplot as plt
plt.figure(figsize=(10, 10))
img = cv2.imread('S2.jpg')
img = cv2.resize(img,(550,550))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,threshold = cv2.threshold(gray, 147, 240, cv2.THRESH_BINARY_INV)
contours,_ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
i = 0
for contour in contours:
    if i == 0:
        i = 1
        continue
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [contour], 0, (100, 100, 210), 5)
    M = cv2.moments(contour)
    if M['m00'] != 0.0:
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])-10
    if len(approx) == 3:
        cv2.putText(img, 'Triangle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (210, 0, 100), 2)
    elif len(approx) == 4:
        cv2.putText(img, 'Quadilateral', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0,100), 2)
    elif len(approx) == 5:
        cv2.putText(img, 'Pentagon', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 0, 200), 2)
    elif len(approx) == 6:
        cv2.putText(img, 'Hexagon', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 200, 0), 2)
    elif len(approx) == 8:
        cv2.putText(img, 'Octagon', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 200, 0), 2)
    else:
        cv2.putText(img, 'circle', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (25, 205, 25), 2)
plt.subplot(1,1,1)
plt.imshow(img)
plt.title("Contours")
plt.xticks([]),plt.yticks([])
plt.show()