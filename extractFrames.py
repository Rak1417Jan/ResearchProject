import os
import cv2


def extract_frames(video_path, output_folder, interval=100):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Initialize variables
    frame_count = 0
    success = True

    # Loop through video frames
    while success:
        # Read a frame from the video
        success, frame = cap.read()

        # Check if the frame was read successfully
        if success:
            # Save the frame at the specified interval
            if frame_count % interval == 0:
                frame_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
                cv2.imwrite(frame_path, frame)

            frame_count += 1

    # Release the video capture object
    cap.release()

