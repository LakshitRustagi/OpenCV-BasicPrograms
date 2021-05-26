import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("The device is not initialised")
    exit()

# cap.set(Property Id , value) enables us to change the value of a property of the video
cap.set(3, 64) # For Width
cap.set(4, 40) # For height
cap.set(10, 1) # For Brightness

while True:
    success, frame = cap.read()

    if not success:
        continue

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()