from rest_framework import viewsets # new
from rest_framework.settings import perform_import
from .models import * 
from .serializers import *
from .permissions import IsAuthorOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet): # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
