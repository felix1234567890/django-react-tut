from articles.models import Article
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    """
    Serializer for the Article model.

    Converts Article model instances to/from JSON and handles validation.
    """
    title = serializers.CharField(
        max_length=120,
        required=True,
        error_messages={
            'required': 'Please provide a title for the article.',
            'max_length': 'Title cannot be more than 120 characters.'
        }
    )
    content = serializers.CharField(
        required=True,
        error_messages={
            'required': 'Please provide content for the article.'
        }
    )
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_title(self, value):
        """
        Validate that the title is not just whitespace.
        """
        if value.strip() == '':
            raise serializers.ValidationError("Title cannot be empty or just whitespace.")
        return value

    def validate_content(self, value):
        """
        Validate that the content is not just whitespace and has a minimum length.
        """
        if value.strip() == '':
            raise serializers.ValidationError("Content cannot be empty or just whitespace.")
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Content must be at least 10 characters long.")
        return value