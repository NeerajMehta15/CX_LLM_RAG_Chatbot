from transformers import AutoModelForCausalLM, AutoTokenizer
from src.utils.config import Config
import torch

class LlamaModel:
    def __init__(self,model_name = Config.HUGGING_FACE_MODEL):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name,torch_dtype = torch.float16, device_map ='auto')

    def generate_response(self, prompt, max_length=200):
        """Generate response using Llama model"""
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        
        outputs = self.model.generate(
            **inputs, 
            max_length=max_length, 
            num_return_sequences=1,
            temperature=0.7
        )
        
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)