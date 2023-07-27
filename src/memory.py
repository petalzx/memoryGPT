from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Memory:
    def __init__(self):
        self.memory = []

    def save_interaction(self, user_message, bot_response):
        # Append the current interaction to the memory list
        self.memory.append((user_message, bot_response))

    def find_similar_response(self, user_message, similarity_threshold=0.7):
        # Retrieve a response from memory based on user input similarity
        for mem_user_message, mem_bot_response in reversed(self.memory):
            similarity = self.compare_texts(user_message, mem_user_message)
            if similarity > similarity_threshold:
                return mem_bot_response

        # If no similar previous user message found, return None
        return None

    def compare_texts(self, text1, text2):
        vectorizer = CountVectorizer().fit_transform([text1, text2])

        # Calculate the cosine similarity between the vectors
        similarity = cosine_similarity(vectorizer[0], vectorizer[1])[0][0]

        return similarity