# **Deepfake Detection & NSFW Content Analysis**

## **Overview**
This project implements a two-fold approach to ensure content safety and authenticity:

### **1. Proactive Approach**  
- **Objective**: Analyze videos for NSFW content by checking both visual and audio elements.
- **Technologies Used**:
  - **Hugging Face Models**:
    - **Whisper**: For audio analysis
    - **FalconsAI Image NSFW Detector**: To check for explicit content in video frames
  - **GROQ Cloud**:
    - **Llama 3 70B**: Used for contextual analysis

### **2. Reactive Approach**  
- **Objective**: Detect whether a video is real or deepfake using image classification techniques.
- **Technologies Used**:
  - **ResNet-50**: For deepfake detection
  - **TensorFlow**: Model training and inference
  - **Python**: Implementation and scripting

## **Usage**
- **NSFW Analysis**: Evaluates a video's audio and images for inappropriate content.
- **Deepfake Detection**: Classifies a video as real or forged using ResNet-50.


## **Future Enhancements**
- Improve model accuracy with larger datasets.
- Optimize processing speed using parallel computing.
- Deploy as a web API for real-time video analysis.

## **Contributors**
- Rakshit Jangid
- Shreya Sachdeva
- Chinmayi Purohit
