import cv2
import numpy as np
from utilidades import image
from utilidades import coordinates


image = cv2.imread("ajustment_image.jpg")
lane_image = np.copy(image)
canny_image = image.canny(lane_image)
cropped = coordinates.region(canny_image)
lines = cv2.HoughLinesP(cropped, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=10500)
average_lines = coordinates.average_slope_intercept(image, lines)
line_image = image.display(image, average_lines)
combo_image = cv2.addWeighted(image, 0.8, line_image, 1, 1)
cv2.imshow("result", combo_image)
cv2.waitKey(1)
