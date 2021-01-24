from PIL import Image
import numpy
import pywt
import sys
import cv2

def estimate_blur(image: numpy.array, threshold: int = 100):
    if image.ndim == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blur_map = cv2.Laplacian(image, cv2.CV_64F)
    score = numpy.var(blur_map)
    return blur_map, score, bool(score < threshold)

def sideBlur(middleImage,sideImage):
    
    if isinstance(middleImage, str):
        image_path = middleImage
        middleImage = cv2.imread(str(image_path))

    if isinstance(sideImage, str):
        image_path = sideImage
        sideImage = cv2.imread(str(image_path))


    blur_map, score, blurry = estimate_blur(middleImage, threshold=100)
    print('Middle Image: score: '+str(score)+' ')
    #blurry should be at least 50% worse than notblurry
    threshold_blurr = int(score)*0.5

    blur_map, score, blurry = estimate_blur(sideImage, threshold=threshold_blurr)
    print('Side Image: score: '+str(score)+'  blurry: '+str(blurry)+' ')

    return blurry