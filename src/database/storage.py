import pandas as pd
from src.embeddings.preprocessing import load_and_preprocess_data
from src.embeddings.embeddings import EmbeddingsGenerator
from src.database.chroma_client import ChromaDBClient

def prepare_vector_database(csv_path):
    '''Prepare vector database from the CSV'''

    #Load and preprocess data
    df = load_and_preprocess_data(csv_path)

    #Generate embeddings
    embeddings_generator = EmbeddingsGenerator()
    embeddings = embeddings_generator.generate_embeddings(df['clean_question'].to_list())

    #Initialize ChromaDB client
    chroma_client = ChromaDBClient()
    collection = chroma_client.create_collection('resident_FAQs')

    #Upsert embeddings
    chroma_client.upsert_embeddings(
        collection,
        ids=[str(i) for i in range(len(df))],
        embeddings=embeddings.tolist(),
        metadatas=[
            {
                'question': q, 
                'answer': a, 
                'cleaned_question': cq
            } for q, a, cq in zip(df['question'], df['answer'], df['cleaned_question'])
        ]
    )
    