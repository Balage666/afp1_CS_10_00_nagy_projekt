from django.shortcuts import render
import openai
from django.shortcuts import render
from openai import chat

api_key="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"
URL = "https://chatgpt-api.shn.hk/v1/"
default =""
def chatbot(request):
    chatbot_response = None
    if request.method == 'POST':
        #URL = "https://chatgpt-api.shn.hk/v1/ \-H 'Content-Type: application/json' \-d '{   model": "gpt-3.5-turbo",   "messages": [{"role": "user", "content": "Hello, how are you?"}]}'"
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt = user_input
        response = chat.completions.create(
        messages = [{"role": "user", "content": user_input}],
        model="gpt-3.5-turbo-1106",
        max_tokens = 256,
        temperature=0.5,
        )
        
        chatbot_response=str(response.choices[0].message.content)
        return render(request, "gpt.html",{"response":chatbot_response})
    else:
        return render(request, "gpt.html",{"response":default})