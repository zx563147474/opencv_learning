import cv2
import numpy as np

img = cv2.imread('handwriting.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))


cv2.drawContours(img, contours, -1, (255, 0, 10), 2)
cv2.imshow('image1', img)
cv2.waitKey(0)

print(hierarchy)


#%%
img2 = cv2.imread('hierarchy.jpg')
img_gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
_, thresh2 = cv2.threshold(img_gray2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

contours2, hierarchy2 = cv2.findContours(thresh2, cv2.RETR_LIST, 2)

print(len(contours2),hierarchy2)
cv2.drawContours(img2, contours2, -1, (0, 0, 255), 2)


cv2.imshow('image2', img2)
cv2.waitKey(0)

#%% practice
img3 = cv2.imread('circle_ring.jpg')
img_gray3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
_, thresh3 = cv2.threshold(img_gray3, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
contours3, hierarchy3 = cv2.findContours(thresh3, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img3, contours3, 0, (180,215,215),-1)
cv2.drawContours(img3, contours3, 1, (0, 0, 200),2)
cv2.drawContours(img3, contours3, 2, (180,215,215),-1)
cv2.drawContours(img3, contours3, 3, (180,215,215),-1)
cv2.drawContours(img3, contours3, 4, (100, 0, 0),2)
cv2.drawContours(img3, contours3, 5, (200, 0, 0),2) #0 2 3

cv2.imshow('image3', img3)
cv2.waitKey(0)

#%%
img4 = cv2.imread('handwriting1.jpg', 0)

_, thresh4 = cv2.threshold(img4, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
contours4, hierarchy4 = cv2.findContours(thresh4, cv2.RETR_LIST, 2)
cnt = contours4[0]
print(cnt)
cv2.imshow('image4', thresh4)
cv2.waitKey(0)

pixels = cv2.countNonZero(thresh4)
img_color1 = cv2.cvtColor(img4, cv2.COLOR_GRAY2BGR)
img_color2 = np.copy(img_color1)
img1=cv2.drawContours(img_color2, [cnt], 0, (0, 0, 255), 2)

cv2.imshow('image4', img1)
cv2.waitKey(0)
area4 = cv2.contourArea(cnt)
perimeter4 = cv2.arcLength(cnt, True) #second parameter means if edge is closed
M4 = cv2.moments(cnt)
cx, cy = M4['m10'] / M4['m00'], M4['m01'] / M4['m00']
print(area4, perimeter4, M4, cx, cy)

x, y, w, h = cv2.boundingRect(cnt)  #
img5 = cv2.rectangle(img_color2, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('image5', img5)
cv2.waitKey(0)

rect = cv2.minAreaRect(cnt)  # minimum rect
box = np.int0(cv2.boxPoints(rect))  #
img6 = cv2.drawContours(img_color1, [box], 0, (255, 0, 0), 2)
cv2.imshow('image6', img6)
cv2.waitKey(0)

(x1, y1), radius = cv2.minEnclosingCircle(cnt)
(x1, y1, radius) = np.int0((x1, y1, radius))  # centroid and radius
img7 = cv2.circle(img_color1, (x1, y1), radius, (0, 0, 255), 2)
cv2.imshow('image7', img7)
cv2.waitKey(0)

ellipse4 = cv2.fitEllipse(cnt)
img8 = cv2.ellipse(img_color2, ellipse4, (255, 255, 0), 2)
cv2.imshow('image8', img8)
cv2.waitKey(0)
#%%
img9 = cv2.imread('shapes.jpg', 0)
_, thresh9 = cv2.threshold(img9, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
contours9, hierarchy9 = cv2.findContours(thresh9, 3, 2)
img_color9 = cv2.cvtColor(thresh9, cv2.COLOR_GRAY2BGR)
cnt_a, cnt_b, cnt_c = contours9[0], contours9[1], contours9[2]
print(cv2.matchShapes(cnt_b, cnt_b, 1, 0.0))
print(cv2.matchShapes(cnt_b, cnt_c, 1, 0.0))
print(cv2.matchShapes(cnt_b, cnt_a, 1, 0.0))