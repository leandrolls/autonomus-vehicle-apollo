import cv2
import numpy as np
import matplotlib.pyplot as plt
from utilidades import image


def region(view):
    height = view.shape[0]
    polygons = np.array([
        [(30, height), (600, height), (300, 120)]
    ])
    mask = np.zeros_like(view)
    cv2.fillPoly(mask, polygons, 255)
    masked = cv2.bitwise_and(view, mask)
    return masked


def average_slope_intercept(view, lines):
    left_fit = []
    right_fit = []
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            parameters = np.polyfit((x1, x2), (y1, y2), 1)
            slope = parameters[0]
            intercept = parameters[1]
            if slope < 0:
                left_fit.append((slope, intercept))
            else:
                right_fit.append((slope, intercept))
    left_fit_average = np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis=0)
    left_line = coordinates(view, left_fit_average)
    right_line = coordinates(view, right_fit_average)
    return np.array([left_line, right_line])


def coordinates(view, line_parameters):

    try:
        slope, intercept = line_parameters
    except TypeError:
        slope, intercept = 0.00001, 0.00001

    y1 = view.shape[0]
    y2 = int(y1 * (3 / 5))
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    return np.array([x1, y1, x2, y2])


# def setImage():
#     plt.imshow("result", region(image.canny()))
#     plt.show()
