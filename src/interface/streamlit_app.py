import streamlit as st
from src.database.storage import prepare_vector_database
from src.llm.model import LlamaModel
from src.llm.rag import RAGSystem
from src.llm.response_generator import ResponseGenerator

def initialize_chatbot():
    """Initialize chatbot component"""

    # Prepare vector database
    collection = prepare_vector_database('data/raw/faqs.csv')
    
    # Initialize LLM
    llm_model = LlamaModel()
    
    # Create RAG system
    rag_system = RAGSystem(collection, llm_model)
    
    return rag_system

def main():
    st.title("Stanza Living - Resident Support Chatbot")
    
    # Initialize chatbot
    rag_system = initialize_chatbot()
    
    # Chat input
    user_query = st.text_input("Ask your query:")
    
    if user_query:
        
        # Generate response
        response = rag_system.generate_augmented_response(user_query)
        
        # Format response
        formatted_response = ResponseGenerator.format_response(response)
        
        # Display response
        st.write("Chatbot:", formatted_response['text'])
        st.write(f"Confidence: {formatted_response['confidence']:.2%}")

if __name__ == "__main__":
    main()