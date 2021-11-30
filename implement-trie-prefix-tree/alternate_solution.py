class Trie(object):

    def __init__(self):
        self.reference_dict = {}
        self.word = None
        self.word_end = False

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self
        curr_word = ""
        for x in range(0, len(word)):
            letter = word[x]
            curr_word += letter
            next_trie = curr.reference_dict.get(curr_word, None)
            if next_trie is None:
                trie = Trie()
                trie.word = curr_word
                curr.reference_dict[curr_word] = trie
                curr = trie
            else:
                curr = next_trie
        curr.word_end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        result, word_end = self.searchEnd(word)
        return result and word_end

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        result, word_end = self.searchEnd(prefix)
        return result

    def searchEnd(self, word):
        search = ""
        curr = self
        x = 0
        while x < len(word):
            search += word[x]
            curr = curr.reference_dict.get(search)
            x += 1
            if not curr:
                break
        return curr, curr.word_end if curr is not None else False
