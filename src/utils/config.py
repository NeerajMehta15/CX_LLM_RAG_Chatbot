# src/utils/config.py
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # LLM Configuration
    HUGGING_FACE_MODEL = os.getenv('HUGGING_FACE_MODEL', 'meta-llama/Llama-3-8B-Instruct')
    
    # Database Configuration
    CHROMA_HOST = os.getenv('CHROMA_HOST', 'localhost')
    CHROMA_PORT = os.getenv('CHROMA_PORT', '8000')
    
    # Embedding Configuration
    EMBEDDING_MODEL = os.getenv('EMBEDDING_MODEL', 'sentence-transformers/all-MiniLM-L6-v2')
    
    # Logging Configuration
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

# Configure logging
def setup_logging():
    log_level = Config.LOG_LEVEL
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        numeric_level = logging.INFO
    
    logging.basicConfig(
        level=numeric_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    return logging.getLogger(__name__)

# Initialize logger
logger = setup_logging()