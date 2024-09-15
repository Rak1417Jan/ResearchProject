import cv2
from detectionModels import face_cascade
import os

def extract_frames_with_faces(video_path, output_path):
    # Load the video
    video_capture = cv2.VideoCapture(video_path)
    frame_count = 0

    # Loop through the video frames
    while True:
        # Read a frame from the video
        ret, frame = video_capture.read()

        # Break the loop if no frame is captured
        if not ret:
            break

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        # If faces are detected, crop the frame to include only the face
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                # Crop the face region
                face_roi = frame[y:y+h, x:x+w]
                # Save the cropped face
                cv2.imwrite(os.path.join(output_path, f"face_{frame_count}.jpg"), face_roi)
                frame_count += 1

    # Release the video capture object
    video_capture.release()