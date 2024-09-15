import os

from huggingface_hub import login
hf_token = os.environ.get('HF_AUTH_TOKEN')

# Login to Hugging Face
login(token=hf_token)