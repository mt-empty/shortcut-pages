# OpenCV Python

> Source: http://opencv.org/

> Aliases: python-opencv, python-computer-vision, computer-vision, computer-vision-python, opencvpython

$ Let's get started
    `import cv2                    {{Import OpenCV Module}} 

$ Basic Operations on Images
    `img = cv2.imread('image.jpg') {{Read File}} 
    `cv2.imshow('Image',img)       {{Show Image 'img' with Title 'Image'}} 
    `img.shape                     {{Return a Tuple of Number of Rows, Columns and Channels (if 'img' is color)}} 
    `img.size                      {{Total Number of Pixels}} 
    `b,g,r = cv2.split(img)        {{Split Image Channels}} 
    `img = cv2.merge(b,g,r)        {{Merge Image Channels}} 

$ Color Spaces
    `hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
>                                  {{Convert the Image to the HSV Color Space}} 
    `lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
>                                  {{Convert the Image to the L*a*b* Color Space}} 
    `gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
>                                  {{Convert the Image to Grayscale}} 

$ Rotation
    `(h, w) = img.shape[:2]
(cX, cY) = (w / 2, h / 2)
>                                  {{Calculate the Center of the Image}} 
    `degrees = 45
M = cv2.getRotationMatrix2D((cX, cY), degrees, 1.0)
>                                  {{Calculate an Affine Matrix of 2D Rotation}} 
    `rotated = cv2.warpAffine(image, M, (w, h))
>                                  {{Apply an Affine Transformation to the Image. In this Case, Rotate Image by 45 Degrees}} 

