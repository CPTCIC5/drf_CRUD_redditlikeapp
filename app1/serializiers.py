from rest_framework import serializers
from .models import Post,Vote

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields= '__all__'


        read_only=['id','pk','author']

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vote
        fields= ['id']
