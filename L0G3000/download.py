import os
os.environ['HF_ENDPOINT']='https://hf-mirror.com'
os.environ['TRANSFORMERS_CACHE']='L0G3000/cache'

from transformers import AutoModel

model = AutoModel.from_pretrained('internlm/internlm2-chat-1_8b', trust_remote_code=True)



