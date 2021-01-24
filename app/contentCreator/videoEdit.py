from pytube import YouTube

#https://readthedocs.org/projects/pyscenedetect-manual/downloads/pdf/latest/ DOKU
from scenedetect import VideoManager
from scenedetect import SceneManager

#for cutting
from scenedetect import video_splitter

# For content-aware scene detection:
from scenedetect.detectors import ContentDetector

#moviepy for cutting https://zulko.github.io/moviepy/ref/videofx/moviepy.video.fx.all.crop.html
from moviepy.editor import *
from moviepy.video.fx.all import crop
import gizeh #animation?

#own Imports
from detectBlurr import sideBlur
from fixedDrawing import circle

import cv2
import numpy as np
import os


def find_scenes(video_path, threshold=60.0):
    # Create our video & scene managers, then add the detector.
    video_manager = VideoManager([video_path])
    scene_manager = SceneManager()
    scene_manager.add_detector(
    ContentDetector(threshold=threshold))

    # Base timestamp at frame 0 (required to obtain the scene list).
    base_timecode = video_manager.get_base_timecode()

    # Improve processing speed by downscaling before processing.
    video_manager.set_downscale_factor()

    # Start the video manager and perform the scene detection.
    video_manager.start()
    scene_manager.detect_scenes(frame_source=video_manager)

    # Each returned scene is a tuple of the (start, end) timecode.
    return scene_manager.get_scene_list(base_timecode)

def saveClip(clip,path,name):
    clip.write_videofile(path+name+'.mp4',codec='mpeg4',audio_codec='aac',bitrate='15000k',ffmpeg_params=["-crf", "0", "-codec:v", "mpeg4"])
    print('saved as: '+path+''+name+'.mp4')

def cropClipsForTikTok(main_clip):
    (W,H) = main_clip.size
    print(W)
    print(H)
    new_W = H * (9/17)
    crop(main_clip, x_center=W/2 , y_center=H/2, width=new_W, height=H)
    cropped_clip = crop(main_clip, x_center=W/2 , y_center=H/2, width=new_W, height=H)
    return cropped_clip

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

def createOutro(clip):

    time_tfreez = clip.duration-0.1
    tfreeze = cvsecs(time_tfreez)

    #clip_before = clip.subclip(0,tfreeze)

    #creates a 3 second freeze clip
    outro = clip.to_ImageClip(tfreeze).set_duration(2).add_mask()

    W,H = outro.size

    outro_bg = ImageClip("movie_assets/img/outro_bg.png").resize( (W,H) )
    
    outro.mask.get_frame = lambda t: circle(screensize=(W,H),
                                       center=(W/2,H/2),
                                       radius=max(0,int(300-200*t)), blur=4)
    audioclip = AudioFileClip('movie_assets/sounds/davidbain_end-game-fail.wav')
    outro = outro.set_audio(audioclip)

    outro=CompositeVideoClip([outro_bg.set_duration(outro.duration),outro],size =clip.size)

    final_clip =  concatenate_videoclips([clip,outro])
    return final_clip

def createOverlay(clip,overlayTxt,align='top'):
    #move text by set_position(lambda t: ('center', (50+t)) )
    overlay = TextClip(overlayTxt, color="black",fontsize=40,stroke_color='white',stroke_width=2)
    overlay = overlay.on_color(size=((overlay.w+4,overlay.h+4)),color=(238, 29, 82))
    return CompositeVideoClip([clip,overlay.set_duration(clip.duration-2).crossfadein(1).crossfadeout(1).set_position(('center', (0+(overlay.h*1.25)) ))])


#0 cleanFolders
print("#0 Clean")
deleteOld=True

if deleteOld:
    os.system('rm -r cutted/*')
downloadURL = 'https://www.youtube.com/watch?v=2-7sin5Bdt8'

#1 download video from youtube into Downloads folder
print("#1 download video")
download = YouTube(downloadURL)
videoYT_id = download.video_id
possibleStreams = download.streams.filter(subtype='mp4',progressive=True).order_by('resolution').desc().all()
possibleStreams[0].download(output_path='Downloads',filename=videoYT_id)

#2 detected scences in video
print("#2 detect scenes")
scenes = find_scenes('Downloads/'+videoYT_id+'.mp4',threshold=60.0)

#3 cut scenes and put them into cutted
print("#3 detect scenes")
useffmpeg=True
os.system('mkdir cutted/'+videoYT_id)
if useffmpeg==True & video_splitter.is_ffmpeg_available():
    print("FFMPEG Found")
    video_splitter.split_video_ffmpeg(input_video_paths=['Downloads/'+videoYT_id+'.mp4'],scene_list=scenes,output_file_template="cutted/"+videoYT_id+"/$VIDEO_NAME Scene $SCENE_NUMBER.mp4",video_name=videoYT_id,arg_override='-codec:v mpeg4 -preset veryfast -crf 10 -c:a aac')
else:
    if video_splitter.is_mkvmerge_available():
        print("MKVMerge Found")
        video_splitter.split_video_mkvmerge(input_video_paths=['Downloads/'+videoYT_id+'.mp4'],scene_list=scenes,output_file_template='cutted/'+videoYT_id+'/$VIDEO_NAME Scene $SCENE_NUMBER.mkv',video_name=videoYT_id)

#4 checkForBlurr and crop if blurr
print("#4 check for side blurr")

for root, dirs, files in os.walk("cutted/"+videoYT_id+"/"):
    for filename in files:
        if filename.split('.')[1] == 'mp4':
            try:
                print('started working with file: '+filename)
                clipPath = "cutted/"+videoYT_id+"/"+filename
                video = VideoFileClip(clipPath)
                (W,H) = video.size
                frameToGet = (int(video.fps)*int(video.duration))
                image = video.get_frame(5)
                img_h, img_w, img_x = image.shape
                side = cutImage(image, 0 , 0, int(img_w/4), img_h,cropType='absolutePositions')
                middle = cutImage(image, int(img_w/2) , int(img_h/2), int(img_w/4), img_h,cropType='centered')
                #check for sideBlur
                if sideBlur(middle,side):
                    print('-- blurr detected')
                    finalClip = video
                    #crop
                    finalClip = cropClipsForTikTok(finalClip)
                    #overlay
                    finalClip = createOverlay(finalClip,'Fail of the day')
                    #outro
                    finalClip = createOutro(finalClip)
                    #saveClip
                    saveClip(finalClip,'readyForUpload/',filename.split('.')[0])
            except:
                print('File skipped -> Error with file: '+filename)