from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import MessageSerializer
from api.models import Message
from django.http import JsonResponse

from django.shortcuts import render, HttpResponse

import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = str(os.getenv("OPENAI_KEY"))

# Create your views here.

def Index(request):
    return HttpResponse("My Django Server Running ! - IKESAN")

class MessageListAV(APIView):



    def post(self, request):
        prompt = request.data.get('input_prompt', '')
        messages = request.data.get('history', [])

        def CustomChatGPT(messages, user_input):
            print("line 32", messages)
            messages.append({"role": "user", "content": user_input})
            print("line 34", messages)
            response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = messages
            )
            print("line 39", response)
            ChatGPT_reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": ChatGPT_reply})
            print("line 42", messages)
            return messages

        data = {
            "input_prompt": prompt,
            "gpt_response": CustomChatGPT(messages, prompt)[-1]["content"],
        }

        """
        TEST PROMPT FOR POSTMAN
        {
            "input_prompt" : "Tell me about my car", 
            "history" : [{"role": "user", "content": "My car is a BMW"}, {"role": "user", "content": "My car was built in 1989"}]
        }
        """


        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)