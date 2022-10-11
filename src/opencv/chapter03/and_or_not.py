import cv2
import numpy as np

img1 = cv2.imread('E:\\python_workspace\\python_scripts\\src\\opencv\\img\\roi.jpg')
img2 = cv2.imread('E:\\python_workspace\\python_scripts\\src\\opencv\\img\\icon.png')

rows, cols, channels = img2.shape
# print(rows,cols,channels)

roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
"""
threshold函数作用：
去掉噪，例如过滤很小或很大像素值的图像点
"""
ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)

mask_inv = cv2.bitwise_not(mask)

# cv2.imshow("mask", mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
img2_bg = cv2.bitwise_and(img2, img2, mask=mask_inv)

dst = cv2.add(img1_bg, img2_bg)

img1[0:rows, 0:cols] = dst

cv2.imshow("img1", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
