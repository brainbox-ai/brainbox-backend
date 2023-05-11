from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from brainbox.api.serializers import MessageSerializer
from brainbox.models import Message
from django.http import JsonResponse

import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = str(os.getenv("OPENAI_KEY"))


class MessageListAV(APIView):
    def get(self, request):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request):
        prompt = request.data['input_prompt']
        
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )

        gpt_response = completion.choices[0].message.content
        
        data = {
            "input_prompt": prompt,
            "gpt_response": gpt_response,
        }

        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)