import cv2
import math
import datetime
import numpy as np

radius = 240
margin = 25
center = (center_x, center_y) = (250, 250)

#clock plate
img = np.zeros((500, 500, 3), np.uint8 )
img[:] = (255, 255, 255)
background_color = (0,0,0)
line_color = (0,0,0)
S_color = (0,0,255)
M_color = (0,255,0)
H_color = (255,0,0)
cv2.circle(img, center, radius, background_color, thickness = 5)

points1 = []
points2 = []

#clock ticks
for i in range(60):
    x1 = center_x + radius*math.cos(i*6*np.pi/180)
    y1 = center_y + radius*math.sin(i*6*np.pi/180)
    points1.append((int(x1), int(y1)))

    x2 = center_x + (radius - 15)*math.cos(i*6*np.pi/180)
    y2 = center_y + (radius - 15)*math.sin(i*6*np.pi/180)
    points2.append((int(x2), int(y2)))
    cv2.line(img, points1[i], points2[i], line_color, thickness = 3)

points3 = []
for i in range(12):
    x3 = center_x + (radius - 25)*math.cos(i*30*np.pi/180)
    y3 = center_y + (radius - 25)*math.sin(i*30*np.pi/180)
    points3.append((int(x3), int(y3)))
    cv2.line(img, points1[5*i],points3[i], line_color, thickness = 6)

#plot second, minute, hour
while(1):
    temp = img.copy()

    current_time = datetime.datetime.now()
    second, minute, hour = current_time.second, current_time.minute, current_time.hour
    #second angle
    S_angle = (second * 6 + 270 ) % 360
    S_x = center_x + (radius - margin) * math.cos(S_angle * np.pi / 180)
    S_y = center_y + (radius - margin) * math.sin(S_angle * np.pi / 180)
    cv2.line(temp, center,(int(S_x), int(S_y)), S_color, thickness=3)

    #minute angle
    M_angle =(minute * 6 + 270 + second/60*6) % 360
    M_x = center_x + (radius - margin*3) * math.cos(M_angle * np.pi / 180)
    M_y = center_y + (radius - margin*3) * math.sin(M_angle * np.pi / 180)
    cv2.line(temp, center,(int(M_x), int(M_y)), M_color, thickness=6)

    #hour angle
    H_angle =(hour * 30 + 270 + minute/60*30 ) % 360
    H_x = center_x + (radius - margin*6) * math.cos(H_angle * np.pi / 180)
    H_y = center_y + (radius - margin*6) * math.sin(H_angle * np.pi / 180)
    cv2.line(temp, center,(int(H_x), int(H_y)), H_color, thickness=9)

    #current time
    font = cv2.FONT_HERSHEY_PLAIN
    time_str = current_time.strftime("%m/%d/%Y")
    cv2.putText(img, time_str, (160, 380), font, 2, (0, 0, 0), 2)

    cv2.imshow('clock', temp)
    if cv2.waitKey(30) == 27:
        cv2.destroyAllWindows()
        break