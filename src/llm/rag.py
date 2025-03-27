from src.database.chroma_client import ChromaDBClient
from src.embeddings.embeddings import EmbeddingGenerator
from src.llm.model import LlamaModel

class RAGSystem:
    def __init__(self, chroma_collection, llm_model):
        self.collection = chroma_collection
        self.llm = llm_model
        self.embedding_generator = EmbeddingGenerator()
    
    def retrieve_context(self, query, top_k=3):
        """
        Retrieve relevant context from vector database
        """
        query_embedding = self.embedding_generator.generate_embeddings([query])[0]
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        return results['metadatas'][0]
    
    def generate_augmented_response(self, query):
        """
        Generate response using RAG
        """
        # Retrieve context
        contexts = self.retrieve_context(query)
        
        # Construct prompt with context
        context_str = "\n".join([
            f"Question: {ctx['question']}\nAnswer: {ctx['answer']}" 
            for ctx in contexts
        ])
        
        prompt = f"""
        Context: {context_str}
        
        User Query: {query}
        
        Based on the context, provide a helpful and concise answer to the user's query:
        """
        
        # Generate response
        response = self.llm.generate_response(prompt)
        
        return response