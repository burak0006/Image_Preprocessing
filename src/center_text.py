import numpy as np
import string
import pickle
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

'''
Setting a single object in the center of the image
in binarized form. It is designed for putting the 
single object in the center of the image, particularly 
for data scientists to align the letters or digits 
within the image constraint to prepare a suitable dataset 
for OCR. It is only for the single object as it is binarized
for background to 0 and foreground to 255. 

Input
test_image     : The image to be processed
desired_width  : Intended width of the image 
desired_height : Intended height of the image

Output
output_image   : The image in which the object is 
aligned to the center

'''

def center_letter(img, desired_width, desired_height):
    # Binary conversion of the gray-scaled image
    th, threshed = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

    # finding contours of the object
    cnts, hierarchy = cv2.findContours(threshed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Extracting the boundaries of the object
    # x:upper left x coordinate of the object
    # y:upper left y coordinate of the object
    # w:width of the object
    # h:height of the object

    M = cv2.moments(cnts[0])
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    x, y, w, h = cv2.boundingRect(cnts[0])

    # if designed height and width of the object are zero, it returns
    # original shape of the image without resizing.

    if desired_height==0 and desired_width==0:
        height, width = img.shape
    else:
        height, width = desired_height, desired_width

    # Creating an empty image and calculating the displacement from the center of new image
    newimg = np.zeros(shape=(height, width), dtype=np.uint8)
    h_new, w_new = int(height / 2), int(width / 2)

    dx = (w_new - cX)
    dy = (h_new - cY)

    xx, yy = x + dx, y + dy
    dst = newimg.copy()

    # Assigning to new image
    dst[yy:yy + h, xx:xx + w] = threshed[y:y + h, x:x + w]

    # Normalization of the image
    dst = dst / 255
    return dst


if __name__ == '__main__':
    
    
    # if you type 0,0, it keeps original size of the image
    # Please note that if the image contains more than single object,
    # it creates error! 
    
    test_image = cv2.imread('../test1.jpg',0)
    output_image = center_letter(test_image,0,0)
    
    cv2.imshow('centered_image',output_image)
    cv2.imshow('original_image',test_image)
    
    cv2.waitKey()

