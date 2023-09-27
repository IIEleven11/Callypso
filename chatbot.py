import openai_api
import voice_model

openai_api_key = "your_openai_api_key_here"

def generate_text_response(text_query):
    response = openai_api.send_request(openai_api_key, text_query)
    return response

def generate_voice_response(text_response):
    voice_model = voice_model.get_voice_model("CallypsoTraining.pth")
    voice_response = voice_model.generate_voice_response(text_response)
    return voice_response

def chat(text_query):
    text_response = generate_text_response(text_query)
    voice_response = generate_voice_response(text_response)
    return voice_response