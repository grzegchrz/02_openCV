import cv2
import random

#open image
img = cv2.imread('image.png')

#view firts row of image
#print(img[0])

#view firts row of image and columns from range 10:100
#print(img[0][10:100])

#manipulation of image - add noise value in firsts rows
for i in range(120):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

resized = cv2.resize(img, (300, 300))
cv2.imshow('Manipulation noise', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(img.shape)


#copy and paste image
tag = img[100:300, 400:600]
img[500:700, 600:800] = tag

resized_copy = cv2.resize(img, (300, 300))
cv2.imshow('MAnipulation copy and paste', resized_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()