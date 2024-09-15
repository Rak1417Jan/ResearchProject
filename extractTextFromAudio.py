import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from datasets import load_dataset
from groq import Groq
import os

def extract_text_from_audio():
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
    model_id = "openai/whisper-large-v3"
    model = AutoModelForSpeechSeq2Seq.from_pretrained(model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=False, use_safetensors=True)
    model.to(device)
    processor = AutoProcessor.from_pretrained(model_id)
    pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    max_new_tokens=128,
    chunk_length_s=25,
    batch_size=16,
    torch_dtype=torch_dtype,
    device=device,
    )
    dataset = load_dataset("distil-whisper/librispeech_long", "clean", split="validation")
    sample = dataset[0]["audio"]
    result = pipe("/content/mydir/extractedAudio/output_audio.mp3")
    text = result["text"]
    client = Groq(
    api_key=os.environ.get('GROQ_API_KEY'),
)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role" : "system",
                "content" : "You are a trained model which when given a text extracted from a video , checks whether the text given does not contain anything which is 'NOT SAFE FOR WORK' NSFW and tells that if the video is suitable to be deepfaked or not , and would or would not destroy anyone's reputation. also the video should not contain any information which if altered can mislead the people seeing it , the information can be political , technical , ethical , non ethical , non political etc. ALSO GIVE ME A NSFW SCORE BETWEEN 0 and 1",
            },
            {
                "role": "user",
                "content": text,
            }
        ],
    model="llama3-70b-8192",
    )

    return chat_completion.choices[0].message.content
