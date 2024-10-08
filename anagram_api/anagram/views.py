from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from anagram.models import Word
from anagram.serializers import (
    WordSerializer,
    AnagramSerializer,
)
from anagram.utils import sorted_words_to_dict


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    @action(
        detail=False,
        methods=["POST"],
        url_path="check-anagram",
        url_name="check_anagram"
    )
    def check_anagram(self, request):
        serializer = AnagramSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            anagram = serializer.validated_data["anagram"]

            words = Word.objects.all()
            sorted_words = sorted_words_to_dict(words)
            if anagram in sorted_words:
                return Response({
                    "message": f"The word is a valid anagram of {sorted_words[anagram]}"
                })
            return Response({"message": "The word is not a valid anagram"})
