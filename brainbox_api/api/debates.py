from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import DebateSerializer
from api.models import Profile

import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = str(os.getenv("OPENAI_KEY"))

class DebateListAV(APIView):
        
    def post(self, request):
        profile = request.data.get('profile', '')
        topic = request.data.get('conversation_topic', '')
        history = request.data.get('history', [])
        
        all_profiles = Profile.objects.all()
        debator = all_profiles.filter(name__icontains=profile)
        print("Line 26:", debator[0].style)
        
        if len(history) == 0:
            prompt = f"In the style of {debator[0].name} with a tone that is {debator[0].style}, provide your views on{topic}"
        else:
            prompt = f"In the style of {debator[0].name} with a tone that is {debator[0].style}, respond to the previous message sent. Provide arguments against the previous message to try and persuade the viewer"
            
        print("Line34:", prompt)
        
        def DebateChatGPT(messages, input):
            messages.append({"role": "user", "content": input})
            response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = messages
            )
            ChatGPT_reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": ChatGPT_reply})
            return messages
        
        data = {
            "conversation_topic": topic,
            "debator": debator[0].id,
            "message": DebateChatGPT(history, prompt)[-1]["content"],
        }
        
        serializer = DebateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    