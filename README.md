# Apollo autonomus vehicle 

# Introduction

Here you will find all the scripts and technologies 
used to build the apollo's autonomous car in partner with [FIAP](https://www.fiap.com.br/) and [Intel](https://www.intel.com.br/content/www/br/pt/homepage.html).

# Index

- [Introduction](#introduction)
- [Our Mission](#our-mission)
- [Getting Started](#getting-started)
  - [Calibration](#calibration)



# Our Mission

In this challenge the Apollo has the mission to build all the system 
to make a car that will be able to ride by yourself attending the traffic
signs and resources of the lane and interact with humans and other vehicles
in the circulation area using Artificial Intelligence, Computer Vision and others technologies.

# Getting Started

## How to use the Apollo Finding Lane ?

First of all it's important to understand that some process are necessary for a better experience.

## Calibration

1. Use the capture.py to capture a photo from the camera device that will be used to identify the lanes.
2. After run the capture.py, an image file will be created with the vision from the camera. With this image created, you must use it to realize the callibration.
3. In the callibration.py you should set the name of the image created by the capture.py. For example, if the image's file name it's "capture.jpg" you should fill the cv2.imread() with it's name, as you can see bellow:

```python
imag = cv2.imread("capture.jpg")
lane_image = np.copy(imag)
canny_image = canny(lane_image)
```

4. After the step 3 made correctly, run the callibration.py file. 
5. You can see that after run it an image with x and y coordinates will be shown. It's important that in this vision shown you can see clearly the lanes that you want to identify.
6. Use this coordinates to fill the np.array() parameters in region() function located in coordinates.py. 
7. You should fill these parameters with the region where the lanes will be seen by the camera.
8. After do the step 7, you can run the finding_video.py script without any worries.

***Note:*** In the finding_video.py and capture.py it's import to check if the correct camera port is set in the cv2.VideoCapture() function.