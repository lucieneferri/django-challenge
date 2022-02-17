from django.shortcuts import render
from rest_framework import viewsets
from serializers import UserSerializer, AuthorSerializer, ArticleSerializer
from models import User, Author, Article
from rest_framework.permissions import IsAdminUser

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class AuthorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()



