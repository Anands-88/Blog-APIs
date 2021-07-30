from django.contrib.auth import get_user_model # new
from rest_framework import serializers
from .models import * # Post, Comment

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id','author','title','body','created_at','updated_at')
        model = Post # from .models.......

class CommentSerializer(serializers.ModelSerializer):

    class Meta: # Used to change the behavior of the Model like changing order options , verbose_name etc...
        fields = ('id','post','body','created_at','updated_at')
        model = Comment
        
class UserSerializer(serializers.ModelSerializer): # new

    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)
        