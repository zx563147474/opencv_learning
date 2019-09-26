import numpy as np
import cv2

img1 = cv2.imread('lena.jpg')
img2 = cv2.imread('opencv-logo-white.png')

rows, cols = img2.shape[:2]
roi = img1[:rows, :cols]
cv2.imshow('ROI', roi)
cv2.waitKey(0)

imgTogray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(imgTogray, 10, 255, cv2.THRESH_BINARY)
cv2.imshow('mask', mask)
cv2.waitKey(0)
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('mixed', mask_inv)
cv2.waitKey(0)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
cv2.imshow('mixed1', img1_bg)
cv2.waitKey(0)

dst = cv2.add(img1_bg, img2)
cv2.imshow('dst', dst)
cv2.waitKey(0)

img1[:rows, :cols] = dst

cv2.imshow('mixed', img1)
cv2.waitKey(0)

# res = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
# cv2.imshow('mixed',res)
# cv2.waitKey(0)