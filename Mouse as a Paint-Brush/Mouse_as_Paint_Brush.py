import cv2
import numpy as np
def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)

img = np.zeros((1024, 1024, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_event)

while(True):
    cv2.imshow('image',img)
    if cv2.waitKey(30) == 27:
        break
cv2.destroyAllWindows()