from typing import List

from anagram.models import Word


def sorted_words_to_dict(words: List[Word]):
    output = {}

    for word in words:
        sorted_word = "".join(sorted(word.value))
        output[sorted_word] = word.value
    return output
