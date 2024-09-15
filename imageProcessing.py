from PIL import Image
import os
from groq import Groq
from detectionModels import classifier
def process_images_in_folder(folder_path):
    total_frames = 0
    sum_nsfw_scores = 0

    # Iterate through all image files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
            image_path = os.path.join(folder_path, filename)
            img = Image.open(image_path)

            # Use the classifier to get the NSFW score
            output = classifier(img)
            nsfw_score = output[1]['score']  # Assuming the NSFW score is the second label in the output

            # Update the total frames and sum of NSFW scores
            total_frames += 1
            sum_nsfw_scores += nsfw_score

    # Calculate the average NSFW score
    average_nsfw_score = sum_nsfw_scores / total_frames if total_frames > 0 else 0


    client = Groq(
        api_key=os.environ.get('GROQ_API_KEY'),
    )


    chat_completion = client.chat.completions.create(
        messages=[

            {
                "role":"system",
                "content":"""Assess the visual content for explicit, suggestive, or inappropriate material.
    Identify any elements that might be considered NSFW, including but not limited to nudity, sexual content, graphic violence, or other sensitive content.
    Contextual Considerations:

    Consider the context in which the image or video is presented. For example, educational content containing explicit material for medical purposes should be treated differently from content intended for exploitation.
    Evaluate the potential for harm or misuse, especially in scenarios where the content could be used for harassment, defamation, or blackmail.
    Ethical Guidelines:

    Prioritize user safety and privacy. Any content that could compromise these principles should be flagged.
    Ensure that the evaluation is unbiased and impartial, respecting cultural and societal norms without imposing unnecessary restrictions.
    NSFW Score Calculation:

    Provide a numerical NSFW score based on the visual analysis, with a higher score indicating higher risk or inappropriateness.
    Include a brief explanation for the assigned score, detailing the factors that influenced the assessment.
    Decision Criteria:

    Classify content as 'Safe', 'Questionable', or 'Unsafe' based on the NSFW score and ethical guidelines.
    Recommend actions for 'Questionable' or 'Unsafe' content, such as further review by a human moderator or automated restriction.
    Evaluate the following image or video according to these guidelines and provide the NSFW score along with your assessment and recommendations"""
            },
            {
                "role": "user",
                "content": "This is the NSFW SCORE THAT I HAVE EVALUATED FOR THE IMAGES"+ str(average_nsfw_score),
            }
        ],
        model="llama3-70b-8192",
    )

    return chat_completion.choices[0].message.content
