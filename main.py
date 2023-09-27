from chatbot import Chatbot

def main():
    chatbot = Chatbot()
    text_query = input("Enter your query: ")
    voice_response = chatbot.generate_response(text_query)
    voice_response.play()

if __name__ == "__main__":
    main()