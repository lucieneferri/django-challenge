from rest_framework import serializers
from api.models import User, Author, Article

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Senha"
    )

    password_confirm = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Confirme a senha"
    )

    is_staff = serializers.BooleanField(
        label="Admin",
        help_text="Indica que usuário consegue acessar o site de administração."
    )
    
    class Meta:
        model = User
        fields = [
            'id_user',
            'username',
            'password',
            'password_confirm',
            'email',
            'is_staff',
            
        ]
    def save(self):

        conta = User(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            is_staff = self.validated_data['is_staff'],
        )

        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']

        if password != password_confirm:
            raise serializers.ValidationError({'password':'Try again'})
        else:
            conta.set_password(password)
            conta.save()
            return conta
    

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class ReadArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    
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

class FullReadArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    
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

class ArticleSerializer(serializers.ModelSerializer):
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