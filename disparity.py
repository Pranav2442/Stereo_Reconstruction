import numpy as np,cv2 as cv 
from matplotlib import pyplot as plt

img_on_left = cv.imread('python\im0.png',0)
img_on_right = cv.imread('python\im1.png',0)
stereo = cv.StereoBM_create(numDisparities=272, blockSize=39)
disparity = stereo.compute(img_on_left,img_on_right)
plt.imshow(disparity,'jet')
plt.xticks([])
plt.yticks([])
plt.show()