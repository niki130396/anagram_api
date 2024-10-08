from rest_framework import viewsets


from anagram.models import Word
from anagram.serializers import WordSerializer


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
