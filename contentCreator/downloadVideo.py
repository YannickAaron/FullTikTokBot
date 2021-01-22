from pytube import YouTube
#download = YouTube('https://www.youtube.com/watch?v=2-7sin5Bdt8').streams.first().download(output_path='Downloads',filename='newVid')

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

def cutClipsForTikTok(clipPath):
    main_clip = VideoFileClip(clipPath)
    W,H = main_clip.size
    new_W = H * (9/17)
    cropped_clip = crop(main_clip, x_center=W/2 , y_center=H/2, width=new_W, height=H)
    cropped_clip.write_videofile('path/to/cropped/video.mp4')

#scenes = find_scenes('Downloads/newVid.mp4')
#print(scenes)
useffmpeg=True
deleteOld=True

if deleteOld:
    import os
    os.system('rm -r cutted/*')

if useffmpeg==True & video_splitter.is_ffmpeg_available():
    print("FFMPEG Found")
    #video_splitter.split_video_ffmpeg(input_video_paths=['Downloads/newVid.mp4'],scene_list=scenes,output_file_template="cutted/$VIDEO_NAME Scene $SCENE_NUMBER.mp4",video_name='Test',arg_override='-codec:v mpeg4 -c:v libx264 -preset veryfast -crf 23 -c:a aac')
else:
    if video_splitter.is_mkvmerge_available():
        print("MKVMerge Found")
        video_splitter.split_video_mkvmerge(input_video_paths=['Downloads/newVid.mp4'],scene_list=scenes,output_file_template='cutted/$VIDEO_NAME Scene $SCENE_NUMBER.mkv',video_name='Test')
