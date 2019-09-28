import cv2
import numpy as np

img = cv2.imread('lena.jpg')

res = np.uint8(np.clip((1.5 * img + 10), 0, 255))
tmp = np.hstack((img, res))
cv2.imshow('image', tmp)
cv2.waitKey(0)

def nothing(x):
    pass
cv2.namedWindow('Image')
img1 = img.copy()
cv2.imshow('Image', img1)
cv2.createTrackbar('Brightness', 'Image', 0, 100, nothing)
cv2.createTrackbar('Contrast', 'Image', 100, 300, nothing)



while (True):
    cv2.imshow('Image', img1)
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        break

    brightNess = cv2.getTrackbarPos('Brightness', 'Image')
    conTrast = cv2.getTrackbarPos('Contrast', 'Image') * 0.01
    img1 = np.uint8(np.clip(conTrast * img + brightNess, 0, 255))



