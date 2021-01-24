import moviepy.editor as mpy
from moviepy.video.fx.all import crop
from detectBlurr import sideBlur
import cv2
import numpy as np
import os

def cutClipsForTikTok(clipPath,name):
    main_clip = mpy.VideoFileClip(clipPath)
    (W,H) = main_clip.size
    print(W)
    print(H)
    new_W = H * (9/17)
    crop(main_clip, x_center=W/2 , y_center=H/2, width=new_W, height=H)
    cropped_clip = crop(main_clip, x_center=W/2 , y_center=H/2, width=new_W, height=H)
    cropped_clip.write_videofile(name+'.mp4',codec='mpeg4')

def cutImage(imageToCut, x , y, width, height,cropType='centered'):
    list_valid_cropyTypes = ['centered','absolutePositions']
    if not isinstance(cropType, str) or cropType not in list_valid_cropyTypes:
        raise ValueError("Wrong cropyType.  'centered' or 'absolutePositions' expected")

    if not isinstance(imageToCut, np.ndarray):
        raise ValueError("Wrong Format: '<np.ndarray>' expected")

    if cropType == 'absolutePositions':
        #y=0 x=0 is the left upper corner, will cut from x and y in the width an height
        #e.g x=0,y=0,width=100,height=100 will result in a 100x100 square startin in the left upper corner
        return imageToCut[y:y+height, x:x+width]
    elif cropType == 'centered':
        #will cut centered from x and y position
        #e.g x=50,y=50,width=100,height=100 will result in a 100x100 square startin in the left upper corner
        return imageToCut[y-int(height/2):y+int(height/2), x-int(width/2):x+int(width/2)]



#cutClipsForTikTok('cutted/testdata.mp4','croppedVid')cd
#print(sideBlur('blurry.png','notblurry.png'))

#np_frame = video.get_frame(2)
video = mpy.VideoFileClip('cutted/testdata.mp4')
(W,H) = video.size
print(video.fps)
print(video.duration)
frameToGet = (int(video.fps)*int(video.duration))
print(frameToGet)
image = video.get_frame(2)
print(type(image))
print(image.shape)


#cutImage(image, 1 , 1, 1, 1)
img_h, img_w, img_x = image.shape
side = cutImage(image, 0 , 0, int(img_w/4), img_h,cropType='absolutePositions')
middle = cutImage(image, int(img_w/2) , int(img_h/2), int(img_w/4), img_h,cropType='centered')

sideBlur(middle,side)
"""
cv2.imshow("side", side)
cv2.imshow("middle", middle)
cv2.waitKey(0)
cv2.imwrite("thumbnail.png", middle)
"""