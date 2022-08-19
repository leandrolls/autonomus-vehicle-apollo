import cv2

cam = cv2.VideoCapture(1)
result, image = cam.read()

if result:
    cv2.imshow("Capture", image)
    cv2.imwrite("capture.jpg", image)
    cv2.waitKey(0)
    cv2.destroyWindow("Capture")

else:
    print("Something happened! Check your camera device.")