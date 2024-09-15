import os
from extractFrames import extract_frames
from imageProcessing import process_images_in_folder
from extractAudio import extract_audio_from_video
from extractTextFromAudio import extract_text_from_audio


def proactive_approach(video_path):
    output_path = '/content/mydir/extractedFrames/'
    os.makedirs(output_path, exist_ok=True)
    extract_frames(video_path,output_path,1)
    judge_image=process_images_in_folder("/content/mydir/newExtractedFrames/")
    extract_audio_from_video(video_path)
    judge_audio=extract_text_from_audio()
    text = "After Judging the NSFW status of the visual part of the video we have the following verdict : "
    bold_text = f"\033[1m{text}\033[0m"
    print(bold_text)
    print(judge_image)
    print("-" * 50)
    text = "After Judging the NSFW status of the audio part of the video we have the following verdict : "
    bold_text = f"\033[1m{text}\033[0m"
    print(bold_text)
    print(judge_audio)
