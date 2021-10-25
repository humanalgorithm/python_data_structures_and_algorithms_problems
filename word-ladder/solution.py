import sys
import Queue
from collections import defaultdict


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        self.word_list_dict = self.preprocess_word_list(wordList, beginWord)
        self.word_queue = Queue.Queue()
        self.word_queue.put((beginWord, 1))
        self.visited_dict = {}
        while not self.word_queue.empty():
            queue_item = self.word_queue.get()
            current_word, level = queue_item[0], queue_item[1]
            if self.visited_dict.get(current_word):
                continue
            if current_word == endWord:
                return level
            available_words = set()
            for trans_key in self.word_list_dict.get(current_word, []):
                available_words.update(self.word_list_dict.get(trans_key, []))
            self.visited_dict[current_word] = True
            for word in available_words:
                self.word_queue.put((word, level + 1))
        return 0

    def get_transformations(self, word):
        transformations = []
        for x in range(0, len(word)):
            new_word = word[0:x] + "*" + word[x + 1:]
            transformations.append(new_word)
        return transformations

    def preprocess_word_list(self, wordList, beginWord):
        word_list_dict = defaultdict(list)
        for word in wordList + [beginWord]:
            transformations = self.get_transformations(word)
            for transformation in transformations:
                if word != beginWord:
                    word_list_dict[transformation].append(word)
            word_list_dict[word] = transformations
        return word_list_dict








