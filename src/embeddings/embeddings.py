from sentence_transformers import SentenceTransformer
from src.utils.config import Config
import logging

class EmbeddingsGenerator:
    def __init__(self, model_name=Config.EMBEDDING_MODEL):
        '''Initialize the model'''
        self.model = SentenceTransformer(model_name)

    def generate_embeddings(self, texts):
        '''Generate embeddings for given text'''
        try:
            embeddings = self.model.encode(texts)  # Corrected variable name
            return embeddings
        except Exception as e:
            logging.error(f"Embedding generation error: {e}")
            return None