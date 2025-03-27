# src/llm/response_generator.py
class ResponseGenerator:
    @staticmethod
    def format_response(response, confidence_score=None):
        """
        Format and enhance the response
        """
        formatted_response = {
            'text': response,
            'confidence': confidence_score or 0.8,
            'sources': []
        }
        return formatted_response