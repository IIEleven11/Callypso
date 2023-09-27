import openai

openai_api_key = "your_openai_api_key_here"

def send_request(text_query):
    openai.api_key = openai_api_key
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=text_query,
      max_tokens=150
    )
    return response.choices[0].text.strip()