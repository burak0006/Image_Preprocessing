# ImagePreprocessing
This repository is a collection of useful image preprocessing tools including text/object-centering, image enhancement, and contour extraction using ```python-opencv```. The python scripts are designed to be used for preprocessing images, particularly for better OCR. 

### Contour Extraction of an Image
A very useful tool for the extraction of objects and their boundaries inside an image. The code extracts all objects within the image with their constraints and further save them all in original form, enabling to extract digits or letter for OCR

### Centering the object
Setting a single object in the centre of the image in binarize form. It is designed for putting the single object in the centre of the image, particularly for data scientists to align the letters or digits within the image constraint to prepare a suitable dataset for OCR. It is only for the single object as it is binarized for the background to 0 and foreground to 255. 

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

Execute following commands for install library:
```sh
$ pip install opencv-python
$ pip install numpy
$ pip install matplotlib
```
You may run each file from terminal by typing the name of the script and change the parameters to obtain the best result

## Results

-Object centering detects the object in binary form and places at the center of the image. It is really useful to create dataset during training for OCR, You may also adapt desired resolution in your project like 28x28 pixels.

<img src="https://github.com/burak0006/ImagePreprocessing/blob/main/test_images/fig1.png" width = "100" height = "200"/> <img src="https://github.com/burak0006/ImagePreprocessing/blob/main/test_images/fig1_centered.png" width="100" height="200"/> <img src="https://github.com/burak0006/ImagePreprocessing/blob/main/test_images/fig2.png" width="300" height="100"/> <img src="https://github.com/burak0006/ImagePreprocessing/blob/main/test_images/fig2_centered.png" width="300" height="100"/>

<img src="https://github.com/burak0006/ImagePreprocessing/blob/main/test_images/test3.jpg?raw=true" width="300" height="100"/> <img src="https://github.com/burak0006/ImagePreprocessing/blob/main/test_images/test3_centered.png?raw=true" width="80" height="80"/> 

-Contour extraction is used to extract digits or letters seperately when required threshold and contour size are selected appropriately.

<img src="https://github.com/burak0006/ImagePreprocessing/blob/main/test_images/card.png" width = "400" height = "300"/> <img src="https://github.com/burak0006/ImagePreprocessing/blob/main/test_images/card_result.jpg" width = "400" height = "300"/> 

-Image Enhancement: I implemented a Gaussian blur technique to remove noise from the image. Please be careful when analyzing your image, you may have to convert BGR to RGB before processing. There are lots of python functions performing several enhancement methods in this repository 

<img src="https://github.com/burak0006/ImagePreprocessing/blob/main/test_images/lena.png" width = "400" height = "300"/> <img src="https://github.com/burak0006/ImagePreprocessing/blob/main/results/lena_blurred.png" width = "400" height = "300"/>





