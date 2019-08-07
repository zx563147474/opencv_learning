import cv2
import numpy as np
events = np.array([i for i in dir(cv2) if 'EVENT' in i])
print(events)