# from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from api.serializers import MessageSerializer, ProfileSerializer
from api.models import Profile
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render, HttpResponse

import random

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
                model="gpt-3.5-turbo",
                messages=messages
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



class RandomMessageListAV(APIView):
    
    def post(self, request):
    
        Characters = ['Donald trump with a funny tone. Respond to previous message.',
                        'Gossip girl, with a scandalous, controversial and shocked tone. Respond to previous message.',
                        'Shakespeare, with an optimistic tone. Respond to previous message.',
                        'Queen Elizabeth the 2nd, with a formal tone. Respond to previous message.',
                        'A 5 year old kid, with a playful tone. Respond to previous message.',
                        'Maya Angelou, with a poetic tone. Respond to previous message.']

        random_character = random.choice(Characters)

        print("line83", random_character ,"/n")
        
        prompt = random_character
        messages = request.data.get('history', [])

        print("line88", prompt ,"/n")
        print("line89", messages ,"/n")


        def CustomChatGPT(messages, user_input):
            print("line 93", messages)
            messages.append({"role": "user", "content": user_input})
            print("line 95", messages)
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            print("line 100", response)
            ChatGPT_reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": ChatGPT_reply})
            print("line 103", messages)
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
          
        """
        redirect_path = reverse("messagelist", args=[random_character])
        print("line93", redirect_path ,"/n")
        # return HttpResponseRedirect(redirect_path)
        return Response({"input_prompt": prompt, "gpt_response": random_character})
        """



class ProfileListAV(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    