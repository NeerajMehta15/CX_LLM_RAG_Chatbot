Project Overview
An AI-powered chatbot to resolve resident queries using RAG and Llama 3.
Setup Instructions

Clone the repository
Create a virtual environment

bashCopypython -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install dependencies

bashCopypip install -r requirements.txt

Prepare your CSV


Place your FAQ CSV in data/raw/faqs.csv
Ensure columns: 'question', 'answer'


Set up environment variables


Create a .env file
Add any necessary configuration variables


Run the application

bashCopystreamlit run main.py
Key Components

LangChain integration
Llama 3 LLM
ChromaDB Vector Database
RAG for intelligent responses

Note
Ensure you have the necessary model access and permissions for Llama 3.
