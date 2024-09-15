import os
from tensorflow import keras
import tensorflow as tf
from extractFacesFrames import extract_frames_with_faces
def reactive_approach(video_path):
    # Load a pre-trained deep learning model for image classification
    model = keras.applications.ResNet50(weights='imagenet')

    # Output directory to save cropped face images
    output_path = '/content/mydir/extractedFrames_withfaces'
    os.makedirs(output_path, exist_ok=True)

    # Extract frames with faces and crop the faces
    extract_frames_with_faces(video_path, output_path)

    # Path to the folder containing video frames
    folder_path = '/content/mydir/extractedFrames_withfaces'

    # Initialize variables
    total_frames = 0
    real = 0
    fake = 0

    # Iterate through all image files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(folder_path, filename)

            # Load and preprocess the image
            image = keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
            image_array = keras.preprocessing.image.img_to_array(image)
            image_array = tf.expand_dims(image_array, 0)
            image_array = keras.applications.resnet50.preprocess_input(image_array)

            # Make predictions on the image
            predictions = model.predict(image_array)
            predicted_label = keras.applications.resnet50.decode_predictions(predictions, top=1)[0][0]

            # Extract confidence score
            confidence_score = predicted_label[2]

            # Update variables based on confidence score
            if confidence_score > 0.25:
                real += 1
            else:
                fake += 1

            total_frames += 1

    # Calculate real score and fake score
    real_score = real / total_frames
    fake_score = fake / total_frames

    # Print variables and scores
    print(f'Total Frames: {total_frames}')
    print(f'Real Frames: {real}')
    print(f'Fake Frames: {fake}')
    print(f'Real Score: {real_score}')
    print(f'Fake Score: {fake_score}')

    if real_score > fake_score:
        print("The video frames tend to have more real frames than fake, hence we judge the video as REAL")
    else:
        print("The video frames tend to have more fake frames than real, hence we judge the video as FAKE")