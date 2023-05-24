from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    input_prompt = models.CharField(max_length=250)
    # creator = models.ForeignKey(User, on_delete=models.CASCADE)
    gpt_response = models.CharField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.input_prompt    

    
class Profile(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class Debate(models.Model):
    conversation_topic = models.CharField(max_length=250)
    debator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    message = models.CharField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.conversation_topic