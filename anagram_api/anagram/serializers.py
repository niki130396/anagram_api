from rest_framework import serializers

from anagram.models import Word


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = "__all__"


class AnagramSerializer(serializers.Serializer):
    anagram = serializers.CharField(max_length=100)
    sorted_anagram = serializers.SerializerMethodField(required=False)

    def get_sorted_anagram(self, obj):
        anagram = obj.get("anagram")
        return "".join(sorted(anagram))
