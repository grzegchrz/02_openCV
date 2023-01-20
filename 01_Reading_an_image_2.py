#import cv2, numpy and matplotlib libraries
import numpy as np
import matplotlib.pyplot as plt
# Python code to read image
import cv2

img = cv2.imread("image.png", cv2.IMREAD_COLOR)

plt.imshow(img)
  