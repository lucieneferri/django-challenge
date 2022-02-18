from rest_framework import serializers
from api.models import User, Author, Article

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id_user',
            'username',
            'password',
            'email',
            'is_staff'
        ]

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id_article',
            'author',
            'category',
            'title',
            'summary',
            'firstParagraph'
        ]

class AdminArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id_article',
            'author',
            'category',
            'title',
            'summary',
            'firstParagraph',
            'body'
        ]