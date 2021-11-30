class Trie(object):

    def __init__(self):
        self.reference_dict = {}
        self.word_end = False

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self
        for x in range(0, len(word)):
            letter = word[x]
            if letter not in curr.reference_dict:
                curr.reference_dict[letter] =  Trie()
            curr = curr.reference_dict.get(letter)
        curr.word_end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self
        for x in range(0, len(word)):
            curr = curr.reference_dict.get(word[x])
            if curr is None:
                return False
        return curr.word_end

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self
        for x in range(0, len(prefix)):
            curr = curr.reference_dict.get(prefix[x])
            if curr is None:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
