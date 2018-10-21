import cv2
from matplotlib import pyplot as plt
import numpy as np
'''
import scipy
from scipy import ndimage
'''

#read image###############################################################
jpg = cv2.imread('jpeg.jpg',0)

##Averaging filter###########################################################
#----by filter2D()----------------------------------
#create a filter matrix with a 7*7 dimension: the bigger the dimension is, the smoother the image is.
kernel = np.ones((7,7),np.float32)/49

#apply filter
linrs = cv2.filter2D(jpg,-1,kernel)

#----by blur()--------------------------------------
blurs = cv2.blur(jpg,(7,7))

##gaussian filter#########################################################
gaurs = cv2.GaussianBlur(jpg,(7,7),0) #a Gaussian fitler with 7*7 dimension

##median filter###########################################################
medrs = cv2.medianBlur(jpg,7)

#show result##############################################################
plt.subplot(231),plt.imshow(jpg,'gray'),plt.title("Original Image")
plt.subplot(232),plt.imshow(linrs,'gray'),plt.title("Linear filter: filter2D()")
plt.subplot(233),plt.imshow(blurs,'gray'),plt.title("Linear filter: blur()")
plt.subplot(234),plt.imshow(gaurs,'gray'),plt.title("Gaussian filter")
plt.subplot(235),plt.imshow(medrs,'gray'),plt.title('Median filter')
plt.savefig("filter result.png")
plt.show()
