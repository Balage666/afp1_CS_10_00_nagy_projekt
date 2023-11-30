from django.shortcuts import render

import requests
import OpenAI
from django.http import JsonResponse

OpenAI.api_key="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"

def index(request):
   return render(request, 'gpt.html')

def api_request_view(request):
    url = 'https://chatgpt-api.shn.hk/v1/'  # Replace with your API endpoint
    
    # Make a GET request to the API
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # Process the API response data as needed
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Failed to fetch data'}, status=500)


client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")