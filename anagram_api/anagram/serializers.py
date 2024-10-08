from rest_framework import serializers

from anagram.models import Word


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = "__all__"


class AnagramSerializer(serializers.Serializer):
    anagram = serializers.CharField(max_length=100)
