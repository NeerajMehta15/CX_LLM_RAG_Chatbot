import chromadb
from chromadb.config import Settings
from src.utils.config import Config
import logging

class ChromaDBClient:
    def __init__(self, host= Config.CHROMA_HOST, port=Config.CHROMA_PORT):
        '''Initialize the ChromaDB client'''
        try:
            self.client = chromadb.Client(host=host, port=port, settings = Settings(allow_reset=True))
        except Exception as e:
            logging.error(f"Error connecting to ChromaDB: {e}")
            self.client = None


    def create_collection(self, collection_name):
        '''Create a collection in the database'''
        try:
            return self.client.create_collection(name= collection_name)
        except Exception as e:
            logging.error(f"Error creating collection: {e}")   
            return None
        
    
    def upsert_embeddings(self, collection, ids, embeddings, metadatas):
        ''' Insert or update embeddings in the database'''
        try:
            collection.upsert(ids = ids, embeddings = embeddings, metadatas = metadatas)
        except Exception as e:
            logging.error(f"Error upserting embeddings: {e}")
            return None
        
    def query_collection(self,collection,query_embedding,n_results=5):
        '''Query the collection with an embedding'''
        try:
            return collection.query(
                query_embeddings=[query_embedding],
                n_results=n_results
            )
        except Exception as e:
            logging.error(f"Error querying collection: {e}")
            return None