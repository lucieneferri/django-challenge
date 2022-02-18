from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import UserSerializer, AuthorSerializer, ArticleSerializer
from api.models import User, Author, Article
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class AuthorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class AdminArticleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

# /api/admin/articles => AdminArticlesViewSet

# /api/articles => ArticleViewSet 