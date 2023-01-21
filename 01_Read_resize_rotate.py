import cv2

img = cv2.imread('image.png', -1)
img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('new_img.png', img)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()