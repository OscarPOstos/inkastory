from rest_framework import serializers
from .models import Story, StoryNode

class StoryNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryNode
        fields = '__all__'

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'