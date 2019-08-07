import cv2
import numpy as np
drawing = False
mode = True
ix, iy = -1, -1

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
#mouse callback
def draw_circle(event, x, y, flag, param):
    global ix, iy, drawing, mode, img

    if event == cv2.EVENT_LBUTTONDOWN:
        img = np.zeros((512, 512, 3), np.uint8)
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            img = np.zeros((512, 512, 3), np.uint8)
            if mode is True:
                cv2.rectangle(img, (ix, iy),(x,y), (255, 0, 0), 4)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode is True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 4)
        else:
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(20)
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
cv2.destroyAllWindows()


