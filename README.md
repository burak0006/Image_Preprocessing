# ImagePreprocessing
This repository is a collection of useful image preprocessing tools including text/object-centering, image enhancement, and contour extraction using ```python-opencv```. The python scripts are designed to be used for preprocessing images, particularly for better OCR. 

### Contour Extraction of an Image
Very useful tool for the extraction of objects and their boundaries inside an image. The code extracts all objects within the image with their constraints and further save them all in original form, enabling to extract digits or letter for OCR

### Centering the object
Setting a single object in the center of the image in binarized form. It is designed for putting the  single object in the center of the image, particularly  for data scientists to align the letters or digits within the image constraint to prepare a suitable dataset for OCR. It is only for the single object as it is binarized for background to 0 and foreground to 255. 

### Image Enhancement
You can also find useful python scripts for image enhancement like morphological_operators, image_blurring, image_gradient, increasing brightness and
contrast 

## Requirements
- Mac OS X or Linux
- Python3(Recommended)
- Python2

## Preparation
### Library
- PIL
- OpenCV 2
- numpy
- matplotlib
- scipy

## Results

Object centering detects the object in binary form and places at the center of image. It is really useful for training when preparing dataset for OCR

<img src="https://github.com/burak0006/ImagePreprocessing/blob/main/test_images/fig1.png" width = "100" height = "200"/> <img src="https://github.com/burak0006/ImagePreprocessing/blob/main/test_images/fig1_centered.png" width="100" height="200"/> <img src="https://github.com/burak0006/ImagePreprocessing/blob/main/test_images/fig2.png" width="300" height="100"/> <img src="https://github.com/burak0006/ImagePreprocessing/blob/main/test_images/fig2_centered.png" width="300" height="100"/> 
