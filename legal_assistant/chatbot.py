# # chatbot.py
# import google.generativeai as genai
# import os
# from dotenv import load_dotenv
# import logging

# # Set up logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

# # Load environment variables
# load_dotenv()

# # Configure the Gemini API
# api_key = os.getenv("GEMINI_API_KEY")
# if not api_key:
#     raise ValueError("GEMINI_API_KEY not found in environment variables")

# genai.configure(api_key=api_key)

# # Set up the model
# model = genai.GenerativeModel('gemini-pro')

# def get_legal_response(query, context=""):
#     prompt = (
#         f"""You are an AI legal assistant.
#         Your role is to provide information and general guidance on legal matters with detailed responses, including relevant IPC sections.
#         Provide information based on general legal principles.
#         should provide a brief answer unless more detail is explicitly requested.
#         Cite relevant laws or cases when possible, and format the response using HTML tags for bold and italic text.
#         If you're unsure about any information, clearly state that.
#         Avoid using bullet points or numbered steps in the response.
#         Provide information in a clear and readable format.
#         Always prefer try to put direct google link of 5 most related Case studies related to query.
        
#         Context: {context}
        
#         Legal aspects for the following query: {query}
#         """
#     )
    
#     try:
#         logger.info(f"Sending query to API: {prompt}")
#         response = model.generate_content(prompt)
#         logger.info(f"Raw API Response Type: {type(response)}")
#         logger.info(f"Raw API Response: {response}")
        
#         # Handle 'Part' type response
#         if hasattr(response, 'parts') and response.parts:
#             text_response = response.parts[0].text
#         elif hasattr(response, 'text'):
#             text_response = response.text
#         else:
#             logger.warning("Unexpected response format")
#             text_response = str(response)
        
#         # Format response text with HTML tags for bold and italic
#         formatted_response = (
#             text_response
#             .replace("**", "<b>")
#         )
        
#         return formatted_response
    
#     except Exception as e:
#         logger.error(f"Error in get_legal_response: {str(e)}")
#         return f"Error: {str(e)}" 

# chatbot.py
import google.generativeai as genai
import os
from dotenv import load_dotenv
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Configure the Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

genai.configure(api_key=api_key)

# Set up the model
model = genai.GenerativeModel('gemini-pro')

def get_legal_response(query, context=""):
    prompt = (
        f"""You are an AI legal assistant.
        Your role is to provide information and general guidance on legal matters with detailed responses, including relevant IPC sections.
        Provide information based on general legal principles.
        should provide a brief answer unless more detail is explicitly requested.
        Cite relevant laws or cases when possible, and format the response using HTML tags for bold and italic text.
        If you're unsure about any information, clearly state that.
        Avoid using bullet points or numbered steps in the response.
        Provide information in a clear and readable format.
        Always prefer try to put working direct google link of 5 most related Case studies related to query.
        
        Context: {context}
        
        Legal aspects for the following query: {query}
        """
    )
    
    try:
        logger.info(f"Sending query to API: {prompt}")
        response = model.generate_content(prompt)
        logger.info(f"Raw API Response Type: {type(response)}")
        logger.info(f"Raw API Response: {response}")
        
        # Handle 'Part' type response
        if hasattr(response, 'parts') and response.parts:
            text_response = response.parts[0].text
        elif hasattr(response, 'text'):
            text_response = response.text
        else:
            logger.warning("Unexpected response format")
            text_response = str(response)
        
        # Format response text with HTML tags for bold and italic
        formatted_response = (
            text_response
            .replace("**", "<b>")
        )
        
        return formatted_response
    
    except Exception as e:
        logger.error(f"Error in get_legal_response: {str(e)}")
        return f"Error: {str(e)}"


