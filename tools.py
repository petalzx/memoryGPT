import openai
from config import OPENAI_API_KEY
import tiktoken
import re

openai.api_key = OPENAI_API_KEY

def get_embedding(text):
    return openai.Embedding.create(input=[text], model = 'text-embedding-ada-002')['data'][0]['embedding']

def get_importance_interaction(message, response):
    importance_response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {'role': 'system', 'content': 'You are the large language model designed to respond to humans. The following is a snippet of a conversation between a user and a chatbot'},
            {'role': 'user', 'content': message},
            {'role': 'assistant', 'content': response},
            {'role': 'system', 'content': 'Please rate the importance of remembering the above interaction on a scale from 1 to 10 where 1 is trivial and 10 is very important. Only respond with the number, do not add any commentary.'},
        ]
        temperature=0,
        n=1,
        max_tokens=100
    )