import cv2

img = cv2.imread('lena.jpg')

# 1.转成灰度图
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img', img)
cv2.imshow('gray', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2.获取所有的转换模式
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)
