from pickle import GET
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from api.serializers import FullReadArticleSerializer, ReadArticleSerializer, UserSerializer, AuthorSerializer, ArticleSerializer
from api.models import User, Author, Article
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

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
   queryset = Article.objects.all()

   def get_permissions(self):
        if(self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']):
           self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = []
        return super(self.__class__, self).get_permissions()
    
   
   def get_serializer_class(self):
        if (self.request.method in ['GET']):
            if self.request.user.is_authenticated == True:
                return FullReadArticleSerializer
            return ReadArticleSerializer
        return ArticleSerializer
