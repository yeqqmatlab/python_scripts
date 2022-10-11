import cv2
import numpy as np

img = cv2.imread('E:\\python_workspace\\python_scripts\\src\\opencv\\img\\roi.jpg')

print(img.shape)

# cv2.imshow("roi", img)

ball = img[280:340, 330:390]

img[273:333, 100:160] = ball

cv2.imshow("roi", img)

cv2.waitKey(0)
