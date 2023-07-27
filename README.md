# memoryGPT

memoryGPT is a project that creates a chatbot that uses openai api to generate responses and Pinecone index to store and retrieve previous interactions between the chatbot and user. The memory-retrieval algorithm fetches the most relevant message-response pairs from its memory based on a composite score. The api model used can be changed in the .env file.

## Setup
1. Clone the repo
2. Install the required dependencies (check requirements.txt)
3. Edit the env file
4. run main.py
