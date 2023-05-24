from rest_framework import serializers
from api.models import Message, Profile, Debate

class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = "__all__"
        

class DebateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Debate
        fields = "__all__"