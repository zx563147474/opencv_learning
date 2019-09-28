import cv2
import numpy as np
#%%
img = cv2.imread('j.bmp', 0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel)

kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
kernel3 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
erosion1 = cv2.erode(img, kernel1)
erosion2 = cv2.erode(img, kernel2)
erosion3 = cv2.erode(img, kernel3)

both = np.hstack((img, erosion, erosion1, erosion2, erosion3))

cv2.imshow('compare', both)
cv2.waitKey(0)
#%%

img1 = cv2.imread('j_noise_out.bmp', 0)
opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel1)
img2 = cv2.imread('j_noise_in.bmp', 0)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

both1 = np.hstack((img1, opening))
cv2.imshow('compare1', both1)
cv2.waitKey(0)

both2 = np.hstack((img2, closing))
cv2.imshow('compare2', both2)
cv2.waitKey(0)

#%%
img3 = cv2.imread('school.bmp', 0)
gradient = cv2.morphologyEx(img3, cv2.MORPH_GRADIENT, kernel1)
tophat = cv2.morphologyEx(img3, cv2.MORPH_TOPHAT, kernel1)
blackhat = cv2.morphologyEx(img3, cv2.MORPH_BLACKHAT, kernel1)
both3 = np.hstack((img3, gradient, tophat, blackhat))
cv2.imshow('compare3', both3)
cv2.waitKey(0)
