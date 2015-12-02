from rest_framework import serializers
from blog.models import User, Post 
from products.models import Products


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'text']

    def create(self, validate_data):
        return Post.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.author = validate_data.get('author', instance.author)
        instance.title = validate_data.get('title', instance.title)
        instance.text = validate_data.get('text', instance.text)
        instance.save()
        return instance


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ['id', 'title', 'description', 'price']

    def create(self, validate_data):
        return Products.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.title = validate_data.get('title', instance.title)
        instance.description = validate_data.get('description', instance.description)
        instance.price = validate_data.get('price', instance.price)
        instance.save()
        return instance


