import numpy as np
img = np.zeros((5,4,3), np.uint8)
img[:] = (1, 2, 3)
print(img)
print(img[:,:,1])