import cv2
import numpy as np

#guassian blur kernal size
guablur_size = 5

#Canny threshold
cLow = 50
cHigh = 150

#Hough transform
r_distance = 0.8
thetaAcc = np.pi / 180
thres = 90
minLLen = 60
maxLGap = 50
#%%
def image_processing(img):

    grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    guassian = cv2.GaussianBlur(grayScale, (guablur_size, guablur_size), 2)
    edges = cv2.Canny(guassian, cLow, cHigh)

    # create ROI mask
    h, w = edges.shape
    corner_points = np.array([(0, h), (400, 320), (540, 320), (w, h)])
    ROI_mask = ROI(edges, corner_points)

    #Hough
    drawing, lines = Hough_Trans(ROI_mask, r_distance, thetaAcc, thres, minLLen, maxLGap)

    #draw lane lines



    return guassian, edges, ROI_mask, drawing

def ROI(img, corners):

    mask = np.zeros(img.shape, dtype='uint8')
    cv2.fillPoly(mask, [corners], 255)
    #cv2.imshow('compare', np.hstack((img, mask)))
    #cv2.waitKey(0)
    masked = cv2.bitwise_and(img, mask)
    return masked

def Hough_Trans(img, r_distance, theta, thres, minLLen, maxLGap):
    drawing = np.zeros((img.shape[0], img.shape[1],3), dtype= 'uint8')
    lines = cv2.HoughLinesP(img, r_distance, theta, thres, minLineLength = minLLen, maxLineGap = maxLGap)
    draw_lines(drawing, lines)
    cv2.imshow('drawing', drawing)
    cv2.waitKey(0)
    return drawing, lines

def draw_lines(img, lines, color = (0, 255, 0), thickness = 2):
    for line in lines:
        for x1, y1, x2, y2, in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)


if __name__ == '__main__':
    img = cv2.imread('lane.jpg')
    filtered, res, ROImask, drawing = image_processing(img)
    cv2.imshow('compare',np.hstack((filtered, res, ROImask)))
    cv2.waitKey(0)


