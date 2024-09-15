from moviepy.editor import VideoFileClip

def extract_audio_from_video(video_path):
    # Path to the input video file
    video_file_path = video_path

    # Path to the output audio file
    audio_file_path = '/content/mydir/extractedAudio/output_audio.mp3'

    # Load the video file
    video = VideoFileClip(video_file_path)

    # Extract the audio from the video
    audio = video.audio

    # Write the audio to a file
    audio.write_audiofile(audio_file_path)

    # Close the video and audio objects
    video.close()
    audio.close()

    print(f"Audio extracted and saved to {audio_file_path}")