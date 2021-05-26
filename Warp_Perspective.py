import cv2
import numpy as np

img = cv2.imread('cards.jpg')
width, height = 500, 600
pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])   # Calculated using Paint
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
img_warp = cv2.warpPerspective(img, matrix ,(width,height))

cv2.imshow("Warped Image", img_warp)
cv2.waitKey(0)

