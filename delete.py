import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2

# image = cv2.imread('um_lane_000000.png')
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# background_color = np.array([255,0,0])
# gt_bg = np.all(image == background_color, axis=2)
# gt_bg = gt_bg.reshape(*gt_bg.shape, 1)
# gt_image = np.concatenate((gt_bg, np.invert(gt_bg)), axis=2)

# print(len(gt_image[0][0]))

a = [[1,2,3], [0,5,6]]
a = np.array([[[0,2,3] for i in range(6)] for j in range(3)])
print(a.shape)
b = (np.all(a == [0,2,3], axis = 2))
print(b.shape)
print(*b.shape)
b = b.reshape(*b.shape,1)
print(b.shape)

b = np.concatenate((b, np.invert(b)), axis=2)
print(b.shape)
