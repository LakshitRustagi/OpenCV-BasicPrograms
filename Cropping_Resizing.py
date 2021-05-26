import cv2

img = cv2.imread("vk.jpg")
print(img.shape)

print(f"The width of the image is {img.shape[1]} and the height is {img.shape[0]}")

imgResized = cv2.resize(img,dsize=(100,500))
print(f"The width of the image is {imgResized.shape[1]} and the height is {imgResized.shape[0]}")

imgCrop = img[100:300,50:150]

cv2.imshow("Image",img)
cv2.imshow("Resized Image",imgResized)
cv2.imshow("Cropped Image",imgCrop)



cv2.waitKey(0)