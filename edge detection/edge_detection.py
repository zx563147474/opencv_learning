import cv2
import numpy as np

img = cv2.imread('handwriting.jpg', 0)
edges = cv2.Canny(img, 30, 70)
both = np.hstack((img, edges))
cv2.imshow('compare',both)
cv2.waitKey(0)

res, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
edges1 = cv2.Canny(thresh, 30, 70)
cv2.imshow('better', np.hstack((img, thresh, edges1)))
cv2.waitKey(0)



def nothing(x):
    pass

img1 = cv2.imread('sudoku.jpg', 0)
cv2.namedWindow('window')

cv2.createTrackbar('maxVal', 'window', 20, 255, nothing)
cv2.createTrackbar('minVal', 'window', 20, 255, nothing)
cv2.imshow('window', img1)

while(True):
    max_val = cv2.getTrackbarPos('maxVal', 'window')
    min_val = cv2.getTrackbarPos('minVal', 'window')

    edges2 = cv2.Canny(img1, min_val, max_val)
    cv2.imshow('window', edges2)

    if cv2.waitKey(30) == 27:
        cv2.destroyAllWindows()
        break