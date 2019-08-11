import cv2

capture = cv2.VideoCapture(0)
FPS = capture.get(5)
print(FPS)
# 定义编码方式并创建VideoWriter对象
fourcc = cv2.VideoWriter_fourcc(*'avc1')
outfile = cv2.VideoWriter('output1.mp4', fourcc, FPS, (640, 480))
while(capture.isOpened()):
    ret, frame = capture.read()
    if ret:
        outfile.write(frame)  # 写入文件
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            capture.release()
            cv2.destroyAllWindows()
            break
    else:
        capture.release()
        cv2.destroyAllWindows()
        break
