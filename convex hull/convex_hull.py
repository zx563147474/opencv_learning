import cv2
import numpy as np

img1 = cv2.imread('unregular.jpg', 0)
image1 = np.copy(img1)
_, thresh1 = cv2.threshold(img1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
contours1, hierarchy1 = cv2.findContours(thresh1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cnt1 = contours1[0]
hull1 = cv2.convexHull(cnt1, returnPoints=True)
print(cv2.isContourConvex(hull1))

approx1 = cv2.approxPolyDP(cnt1, 3, True)  #para 2 means distance from actual contour,
# para 3 means if the contour is closed or not

image1 = cv2.cvtColor(image1, cv2.COLOR_GRAY2BGR)
cv2.polylines(image1, [approx1], True, (0,0,255), 2)
cv2.polylines(image1, [hull1], True, (0,255, 0), 2)
cv2.imshow('original', img1)
cv2.waitKey(0)
cv2.imshow('final', image1)
cv2.waitKey(0)


#%%
img2 = cv2.imread('convex.jpg', 0)
image2 = np.copy(img2)

_, thresh2 = cv2.threshold(img2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
contours2, hierarchy2 = cv2.findContours(thresh2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt2 = contours2[0]
# find corners of hull
hull2 = cv2.convexHull(cnt2, returnPoints=True)
print(cv2.isContourConvex(hull2))
image2 = cv2.cvtColor(image2, cv2.COLOR_GRAY2BGR)
cv2.polylines(image2, [hull2], True, (0, 255, 0), 2)
cv2.imshow('original2', img2)
cv2.waitKey(0)
cv2.imshow('final2', image2)
cv2.waitKey(0)

dist2 = cv2.pointPolygonTest(cnt2, (50, 50), True) #if para 3 is False, it will only give the relative pos
                                                    # -1/0/1 --> is outside/on the line/inside
print(dist2)