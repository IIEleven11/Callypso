1. "openai_api_key": This is the API key for OpenAI GPT-3.5 which will be used in "openai_api.py" and "chatbot.py" to authenticate and make requests to the OpenAI API.

2. "CallypsoTraining.pth": This is the trained voice model file which will be used in "voice_model.py" and "chatbot.py" to generate voice responses.

3. "text_query": This is the user's input text which will be used in "main.py" and "chatbot.py" to generate a response from the chatbot.

4. "voice_response": This is the chatbot's response in voice format, generated in "chatbot.py" and used in "main.py" to output the response.

5. "generate_text_response()": This function in "chatbot.py" uses the OpenAI API to generate a text response based on the user's query. It is called from "main.py".

6. "generate_voice_response()": This function in "voice_model.py" uses the trained voice model to convert the text response into voice. It is called from "chatbot.py".

7. "get_voice_model()": This function in "voice_model.py" loads the trained voice model from "CallypsoTraining.pth". It is called from "chatbot.py".

8. "send_request()": This function in "openai_api.py" sends a request to the OpenAI API and returns the response. It is called from "chatbot.py".