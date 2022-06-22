from dataclasses import field
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        field = ('id', 'title', 'thumbail', 'excerpt', 'content', 'slug', 'published', 'author', 'status')
