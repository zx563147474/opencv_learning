import cv2
import numpy as np
from moviepy.editor import VideoFileClip
#guassian blur kernal size
guablur_size = 5

#Canny threshold
cLow = 50
cHigh = 150

#Hough transform
r_distance = 0.8
thetaAcc = np.pi / 180
thres = 20
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
    #print(lines)
    #draw lane lines
    draw_lane(drawing, lines)
    final = cv2.addWeighted(img, 0.9, drawing, 0.2, 0)
    cv2.imshow('frame', final)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        print('stop')
    return final

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
    #cv2.imshow('drawing', drawing)
    #cv2.waitKey(0)
    return drawing, lines

def draw_lines(img, lines, color = (0, 255, 0), thickness = 2):
    for line in lines:
        for x1, y1, x2, y2, in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)

def draw_lane(img, lines, color = (0, 0, 255), thickness = 5):
    left, right = [], []
    for line in lines:
        for x1, y1, x2, y2 in line:
            slope = (y1 - y2) / (x1 - x2)
            if slope <= 0:
                left.append(line)
            else:
                right.append(line)
    if (len(left) <= 0 or len(right) <= 0):
        print('No line')
        return
    #print('1', left, right)
    clean_wrong_line(left, 0.1)
    clean_wrong_line(right, 0.1)

    left_points = [(x1, y1) for line in left for x1, y1, x2, y2 in line] + \
                  [(x2, y2) for line in left for x1, y1, x2, y2 in line]
    right_points = [(x1, y1) for line in right for x1, y1, x2, y2 in line] + \
                  [(x2, y2) for line in right for x1, y1, x2, y2 in line]
    #print('2',left_points, right_points)
    left_fit_point = least_square(left_points, 320, img.shape[0]) #para 2 is determined by ROI mask
    right_fit_point = least_square(right_points, 320, img.shape[0])
    corners = np.array([[left_fit_point[1], left_fit_point[0], right_fit_point[0], right_fit_point[1]]])
    #print(corners)
    cv2.fillPoly(img, corners, (255, 0, 0))
    # or just the line shape of lane
    # cv2.line(img, left_results[0], left_results[1], (0, 255, 0), thickness)
    # cv2.line(img, right_results[0], right_results[1], (0, 255, 0), thickness)
    #cv2.imshow('filled', img)
    #cv2.waitKey(0)


def least_square(points, ymin, ymax):
    x = [point[0] for point in points]
    y = [point[1] for point in points]

    fit = np.polyfit(y, x, 1)
    fit_fn = np.poly1d(fit)

    xmin = int(fit_fn(ymin))
    xmax = int(fit_fn(ymax))
    return [(xmin, ymin), (xmax, ymax)]


def clean_wrong_line(lines, threshold):
    #
    slope = [(y2 - y1) / (x2 - x1) for line in lines for x1, y1, x2, y2 in line]
    while len(lines) > 0:
        mean = np.mean(slope)
        diff = [abs(s - mean) for s in slope]
        pos = np.argmax(diff)
        if diff[pos] > threshold:
            slope.pop(pos)
            lines.pop(pos)
        else:
            break


if __name__ == '__main__':

    #videoCap = cv2.VideoCapture('cv2_white_lane.mp4')
    #fps = videoCap.get(cv2.CAP_PROP_FPS)
    #fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    #width = int(videoCap.get(cv2.CAP_PROP_FRAME_WIDTH))
    #height = int(videoCap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    #out = cv2.VideoWriter('processed_video.avi', fourcc, fps, (width, height))
    #i = 1
    #while (videoCap.isOpened()):
     #   ret, frame = videoCap.read()
     #   if ret:
    #      _, _, _, _, final = image_processing(frame)
     #       i = i +1
     #       out.write(final)
        #cv2.imshow('current', final)
        #cv2.waitKey(1)
        #if (cv2.waitKey(1) & 0xFF) == ord('q'):  # Hit `q` to exit
        #    break
    #out.release()
    #videoCap.release()
    #cv2.destroyAllWindows()

    #output = 'processed_video.mp4'
    #clip = VideoFileClip('cv2_yellow_lane.mp4')
    #outputVideo = clip.fl_image(image_processing)
    #outputVideo.write_videofile(output, audio=False)

    output = 'processed_video.mp4'
    clip = VideoFileClip("cv2_yellow_lane.mp4")
    out_clip = clip.fl_image(image_processing)
    out_clip.write_videofile(output, audio=False)
    cv2.destroyAllWindows()


