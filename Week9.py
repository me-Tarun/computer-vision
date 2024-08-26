import cv2
from matplotlib import pyplot as plt
img = cv2.imread("M.jpg")
resize = cv2.resize(img,(100,180))
height,width = img.shape[:2]
center = (width/2, height/2)
rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=65, scale=1)
rotated = cv2.warpAffine(src = img, M=rotate_matrix,dsize=(width,height))
enlarge=cv2.resize(img,None,1.5,1.5,cv2.INTER_CUBIC)
l=[img,resize,rotated,enlarge]
t=["Original","Resize","Rotated","Enlarge"]
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(l[i],'gray')
    plt.title(t[i])
    plt.xticks([]),plt.yticks([])
plt.show()