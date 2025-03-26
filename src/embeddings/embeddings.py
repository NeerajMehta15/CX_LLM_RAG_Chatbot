from sentence_transformers import SentenceTransformer
from src.utils.config import Config

class EmbeddingsGenerator:
    def __init__(self,model_name=Config.EMBEDDING_MODEL):
        '''Initialize the model'''
        self.model = SentenceTransformer(model_name)

    def generate_embeddings(self, texts):
        '''Generate embeddings for given text'''
        try:
            emebeddings = self.model.encode(texts)
            return emebeddings
        except Exception as e:
            logging.error(f"Embedding generation error: {e}")
            return None