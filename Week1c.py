import cv2 as cv
from PIL import Image,ImageEnhance
from matplotlib import pyplot as plt
img = Image.open("Odin.webp")
new_brightness_val=-5
new_color_val=-5
new_sharpness_val=-5
new_contrast_val=5
org1 = ImageEnhance.Brightness(img)
new_brightness = org1.enhance(new_brightness_val)
org2=ImageEnhance.Color(img)
new_color=org2.enhance(new_color_val)
org3 = ImageEnhance.Contrast(img)
new_contrast = org3.enhance(new_contrast_val)
org4 = ImageEnhance.Sharpness(img)
new_sharpness = org4.enhance(new_sharpness_val)
l = [img, new_brightness, new_color, new_contrast, new_sharpness]
t = ['Original', 'Brightness', 'Color', 'Contrast', 'Sharpness']
for x in range(5):
    plt.subplot(2, 3, x+1)
    plt.imshow(l[x])
    plt.title(t[x])
    plt.xticks([]), plt.yticks([])
plt.show()