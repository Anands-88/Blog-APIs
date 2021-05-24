from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id','author','title','body','created_at','updated_at')
        model = Post

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id','post','body','created_at','updated_at')
        model = Comment
        