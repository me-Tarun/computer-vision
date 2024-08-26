import cv2 as cv
from matplotlib import pyplot as plt
from PIL import Image,ImageEnhance
plt.figure(figsize=(30, 30))
img=Image.open('Eye.jpg')
low_contrast_val=0.1
med_contrast_val=1
high_contrast_val=2
original=ImageEnhance.Contrast(img)
new_img1=original.enhance(low_contrast_val)
new_img2=original.enhance(med_contrast_val)
new_img3=original.enhance(high_contrast_val)
l=[img,new_img1,new_img2,new_img3]
t=["Original","Low Contrast","Medium Contrast","High Contrast"]
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(l[i])
    plt.title(t[i])
    plt.xticks([]),plt.yticks([])
plt.show()