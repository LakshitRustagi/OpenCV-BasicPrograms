import cv2
import numpy as np

img = np.ones((512,512,3),np.uint8)

# img[:,:,0] = 0
# img[:,:,1] = 0
# img[:,:,2] = 255

# This is same as above
img[:] = 0,0,255

cv2.line(img=img,pt1=(0,0),pt2=(512,512),color=(255,0,0),thickness=2)
cv2.rectangle(img,(128,128),(384,384),(0,255,255),cv2.FILLED)
cv2.rectangle(img,(170,170),(352,352),(0,69,255),1)
cv2.putText(img,"Lakshit",(202,202),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)
cv2.circle(img,(266,266),32,(255,255,255),3)

cv2.imshow("Image", img)

cv2.waitKey(0)