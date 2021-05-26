import cv2
import numpy as np

def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


def getcontours(image):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    print(f"The number of contours in the image are {len(contours)}")

    for cnt in contours:
        area = cv2.contourArea(cnt)
        # Contours with area less than a threshold value will be treated as outliers
        if area > 500:
            print(f"The area is {area}")
            cv2.drawContours(image=imgContour, contours=cnt, contourIdx=-1, color=(100, 100, 10), thickness=2)
            peri = cv2.arcLength(curve=cnt, closed=True)
            print(f"The perimeter is {peri}")
            # approx is a list which contains the positions of all boundary positions
            approx = cv2.approxPolyDP(curve=cnt, epsilon=0.02*peri, closed=True)
            print(f"The contour has {len(approx)} vertices")
            x, y, w, h = cv2.boundingRect(array=approx)
            cv2.rectangle(img=imgContour, pt1=(x, y), pt2=(x+w, y+h), color=(0, 255, 0), thickness=4)
            if len(approx) == 3: objtype = "Triangle"
            elif len(approx) == 4:
                ratio = w/float(h)
                if 0.95 < ratio < 1.05: objtype = "Square"
                else: objtype = "Rectangle"
            elif len(approx) > 4: objtype = "Circle"
            else: objtype = "None"
            cv2.putText(img=imgContour, text=objtype, org=(x+(w//2)-10, y+(h//2)-1),
                        fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, fontScale=0.8, color=(0, 0, 0), thickness=2)

img = cv2.imread("Images/shapes.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img_gray, (3, 3), 1.5)
canny = cv2.Canny(blur, 100, 150)
imgContour = img.copy()

getcontours(canny)

stacked_img = stackImages(0.6, [[img, blur], [canny, imgContour]])
cv2.imshow("Stacked Images", stacked_img)
cv2.waitKey(0)

