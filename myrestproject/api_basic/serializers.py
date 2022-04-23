from wsgiref import validate
from rest_framework import serializers
from api_basic.models import Article

'''
class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    date = serializers.DateTimeField()

    def create(self, validated_data):
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)
        return instance
'''

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        # fields = ['id', 'title', 'author', 'email']
        fields = '__all__'

