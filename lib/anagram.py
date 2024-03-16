#!/usr/bin/env python3

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        anagrams = []
        for w in words:
            if sorted(w.lower()) == sorted(self.word.lower()) and w.lower() != self.word.lower():
                anagrams.append(w)
        return anagrams
