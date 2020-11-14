import numpy as np
import cv2
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

    height, width = img.shape

    # Creating an empty image and calculating the displacement from the center of new image
    newimg = np.zeros(shape=(height, width), dtype=np.uint8)
    h_new, w_new = int(height / 2), int(width / 2)

    dx = (w_new - cX)
    dy = (h_new - cY)

    xx, yy = x + dx, y + dy
    dst = newimg.copy()

    # Assigning to new image
    dst[yy:yy + h, xx:xx + w] = threshed[y:y + h, x:x + w]
    
    template = []

    # Final image with desired resolution
    fimg = np.zeros((desired_height,desired_width),np.uint8)

    if desired_height!=0 and desired_width!=0:

        if desired_height>=h or desired_width>=w:

            template = dst[yy:yy+h,xx:xx+w]

            y = int((desired_height-h)/2)
            x = int((desired_width-w)/2)
            
            # Placing the object in the center of image without resolution loss
            fimg[y:y+h,x:x+w] = template

        else:
            
    # if the height and width of the object are bigger than the desired resolution, it returns original image with centered object

            fimg = dst
            print('The object has higher resolution than desired resolution. Automatically set to original image')

    # Normalization of the image
    fimg = fimg / 255

    return fimg


if __name__ == '__main__':
    
 
    # Please note that if the image contains more than single object,
    # it creates error! 
    
    test_image = cv2.imread('../test1.jpg',0)
    output_image = center_letter(test_image,80,80)
    
    cv2.imshow('centered_image',output_image)
    cv2.imshow('original_image',test_image)
    
    cv2.waitKey()



