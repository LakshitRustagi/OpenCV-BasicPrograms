import cv2
import numpy as np


img = cv2.imread("vk.jpg")
kernel = np.ones((5, 5), np.uint8)


# Converting to grayscale image
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Converting to blur image
# Docs : https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html
# Kernel size must contain positive and odd numbers
blurimg = cv2.GaussianBlur(img, (9, 9), 5)
# For edge detection
# Docs : https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html
cannyimg = cv2.Canny(img, 100, 150)

# Morphological Transformations
# Docs : https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html
# Dilation
dilimg = cv2.dilate(cannyimg, kernel, iterations=1)
# Erosion
eroimg = cv2.erode(dilimg, kernel, iterations=1)

cv2.imshow("Gray Image", grayimg)
cv2.imshow("Blur Image", blurimg)
cv2.imshow("Canny Image", cannyimg)
cv2.imshow("Dilated Image", dilimg)
cv2.imshow("Eroded Image", eroimg)

cv2.waitKey(0)