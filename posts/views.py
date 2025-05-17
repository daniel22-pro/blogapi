# posts/views.py
from rest_framework import generics,permissions
from .models import Post
from .serializers import PostSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet (viewsets.ModelViewSet):
    permission_classes=[IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class=UserSerializer

