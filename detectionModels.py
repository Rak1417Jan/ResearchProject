import cv2
from transformers import pipeline
# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
classifier = pipeline("image-classification", model="Falconsai/nsfw_image_detection")
