import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # LLM Configuration
    HUGGING_FACE_MODEL = os.getenv('HUGGING_FACE_MODEL', 'meta-llama/Llama-2-7b-chat-hf')
    
    # Database Configuration
    CHROMA_HOST = os.getenv('CHROMA_HOST', 'localhost')
    CHROMA_PORT = os.getenv('CHROMA_PORT', '8000')
    
    # Embedding Configuration
    EMBEDDING_MODEL = os.getenv('EMBEDDING_MODEL', 'all-MiniLM-L6-v2')
    
    # Logging Configuration
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

# Logging configuration
import logging
logging.basicConfig(
    level=getattr(logging, Config.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)