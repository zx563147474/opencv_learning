import cv2
import numpy as np

img = cv2.imread('lena.jpg')
blur = cv2.blur(img, (6, 6))
blur1 = cv2.boxFilter(img, -1, (3, 3), normalize=True)
gaussian = cv2.GaussianBlur(img, (5, 5), 2)
bilFi = cv2.bilateralFilter(img, 9, 200, 200)
both = np.hstack((img, blur, blur1, gaussian, bilFi))
cv2.imshow('compare', both)
cv2.waitKey(0)

img1 = cv2.imread('salt_noise.bmp', 0)

blur2 = cv2.blur(img1, (5, 5))  # 均值滤波
median = cv2.medianBlur(img1, 5)  # 中值滤波
both1 = np.hstack((img1, median))
cv2.imshow('compare1', both1)
cv2.waitKey(0)

