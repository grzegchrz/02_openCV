
import numpy as np
import matplotlib.pyplot as plt

import cv2

image = cv2.imread('image.png')

img1 = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

plt.imshow(img1, cmap='gray')

plt.show()