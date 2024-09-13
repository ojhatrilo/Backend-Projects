from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'year']

    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Title is required.")
        return value

    def validate_author(self, value):
        if not value:
            raise serializers.ValidationError("Author is required.")
        return value

    def validate_year(self, value):
        if value < 0:
            raise serializers.ValidationError("Year must be a positive integer.")
        return value
