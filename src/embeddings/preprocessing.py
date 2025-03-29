import re
import pandas as pd
import logging

def clean_text(text):
    '''Clean text by removing unnecessary characters and altering the format of words.'''
    
    # Handle non-string inputs
    if not isinstance(text, str):
        return ""
        
    # Convert to lower case
    text = text.lower()

    # Remove unnecessary characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Remove extra white spaces
    text = ' '.join(text.split())

    return text


def load_and_preprocess_data(file_path):
    '''Load and preprocess data from a file.'''

    try:
        df = pd.read_csv(file_path)

        # Clean question and answer columns
        df['clean_question'] = df['question'].apply(clean_text)
        df['clean_answer'] = df['answer'].apply(clean_text)

        return df
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        return None