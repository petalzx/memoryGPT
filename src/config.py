import os
from dotenv import load_dotenv

def find_parent_env_file():
    current_file_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_file_directory)
    env_file_path = os.path.join(parent_directory, '.env')

    return env_file_path

# Load environment variables from the .env file 
env_file_path = find_parent_env_file()
load_dotenv(dotenv_path=env_file_path)


# Retrieve environment variables with default and required options
def env_variable(name, default = None, required = True):
    value = os.getenv(name, default)
    if required and not value:
        raise ValueError(f"{name} .env is missing the environment variable")
    return value

# Get confguration from the environment variables
OPENAI_API_KEY = env_variable('OPENAI_API_KEY')
PINECONE_API_KEY = env_variable('PINECONE_API_KEY')
PINECONE_ENVIRONMENT = env_variable('PINECONE_ENVIRONMENT')
PINECONE_TABLE_NAME = env_variable('PINECONE_TABLE_NAME')
GPT_MODEL = env_variable('GPT_MODEL', default='gpt-3.5-turbo', required=False)