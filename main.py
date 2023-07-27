import src.processing as processing
from src.config import PINECONE_TABLE_NAME, GPT_MODEL

def main():
    chatbot = processing.Chatbot()

    print("Chatbot: Hi! I'm MemoryGPT, a chatbot with long-term memory. How can I assist you today?")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye!")
            break

        # Get the chatbot's response
        bot_response = chatbot.get_response(user_input)
        print("Chatbot:", bot_response)

if __name__ == "__main__":
    main()