import cv2
import numpy as np

img = cv2.imread('shapes.jpg')
drawing = np.zeros(img.shape[:], dtype=np.uint8)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)
cv2.imshow('edges', edges)
cv2.waitKey(0)

#%%Hough transform
lines = cv2.HoughLines(edges, 0.8, np.pi / 180, 80)
length = 200
drawing1 = np.copy(drawing)
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + length * (-b))
    y1 = int(y0 + length * (a))
    x2 = int(x0 - length * (-b))
    y2 = int(y0 - length * (a))
    cv2.line(drawing1, (x1, y1), (x2, y2), (0, 0, 255),lineType=cv2.LINE_AA)
cv2.imshow('hough lines', np.hstack((img, drawing1)))
cv2.waitKey(0)
#%% Probabilistic Hough Transform
drawing2 = np.copy(drawing)
lines1 = cv2.HoughLinesP(edges, 0.8, np.pi/180, 90, minLineLength=50, maxLineGap=10)
for line in lines1:
    x1, y1, x2, y2 = line[0]
    cv2.line(drawing2, (x1, y1), (x2, y2), (0, 255, 0), 1, lineType=cv2.LINE_AA)

cv2.imshow('Probabilistic Hough Transform',np.hstack((img, drawing2)))
cv2.waitKey(0)
#%%Hough circle
drawing3 = np.copy(drawing)
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 20, param2=30)
circles1 = np.int0(np.around(circles))
for i in circles1[0, :]:
    cv2.circle(drawing3, (i[0], i[1]), i[2], (0, 255, 0), -1, lineType=cv2.LINE_AA)
    cv2.circle(drawing3, (i[0], i[1]), 2, (0, 0, 255), -1)
cv2.imshow('circles', np.hstack((img, drawing3)))
cv2.waitKey(0)