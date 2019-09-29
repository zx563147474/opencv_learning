import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('hist.jpg', 0)

#using openCV
start1 = cv2.getTickCount()
hist = cv2.calcHist([img], [0], None, [256], [0, 255])
end1 = cv2.getTickCount()
costTime1 = end1 - start1
print((costTime1) / cv2.getTickFrequency())
plt.plot(hist)
plt.show()

#%%using numpy
start2 = cv2.getTickCount()
hist2, bins2 = np.histogram(img.ravel(), 256, [0, 256])
end2 = cv2.getTickCount()
costTime2 = end2 - start2
print((costTime2) / cv2.getTickFrequency())
plt.plot(hist2)
plt.show()

start3 = cv2.getTickCount()
hist3 = np.bincount(img.ravel(), minlength=256)
end3 = cv2.getTickCount()
costTime3 = end3 - start3
print((costTime3) / cv2.getTickFrequency())
plt.plot(hist3)
plt.show()
#%%
plt.hist(img.ravel(), 256, [0, 255])
plt.show()

#%%
equ = cv2.equalizeHist(img)
equhist = cv2.calcHist([equ], [0], None, [256], [0, 255])
compare1 = np.hstack((img, equ))
cv2.imshow('compare', compare1)
cv2.waitKey(0)

fig, axs = plt.subplots(2, 2)
axs[0,0].imshow(img, cmap='gray', vmin=0, vmax=255)
axs[0,0].axis('off')

axs[0,1].imshow(equ, cmap='gray', vmin=0, vmax=255)
axs[0,1].axis('off')

axs[1,0].plot(hist)
axs[1,1].plot(equhist)
plt.show()

#%%
img1 = cv2.imread('tsukuba.jpg', 0)
equ = cv2.equalizeHist(img1)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img1)
cv2.imshow('equalization', np.hstack((img1, equ, cl1)))
cv2.waitKey(0)

#%%exercise
mask = np.zeros(img.shape[:2], dtype= 'uint8')
mask[:200,:200] = 255
hist4 = cv2.calcHist([img], [0], mask, [256], [0, 255])
plt.plot(hist4)
plt.show()