from rest_framework import serializers
from blog.models import * 


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'text']

    def create(self, validate_data):
        return Post.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.id = validate_data.get('id', instance.id)
        instance.author = validate_data.get('author', instance.author)
        instance.title = validate_data.get('title', instance.title)
        instance.text = validate_data.get('text', instance.data)
        instance.save()
        return instance



