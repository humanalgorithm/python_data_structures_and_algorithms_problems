class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.word_found = False
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                found = self.word_search(board, word, i, j, "", set())
                if found:
                    return True
        return False

    def word_search(self, board, word, i, j, letters, visited):
        if (i, j) in visited:
            return False
        visited.add((i, j))
        try:
            if i < 0 or j < 0:
                raise Exception
            letter = board[i][j]
            letters = letters + letter
        except:
            return False

        if letters != word[0:len(letters)]:
            visited.remove((i, j))
            return False

        if letters == word:
            return True

        a = self.word_search(board, word, i + 1, j, letters, visited)
        b = self.word_search(board, word, i - 1, j, letters, visited)
        c = self.word_search(board, word, i, j + 1, letters, visited)
        d = self.word_search(board, word, i, j - 1, letters, visited)

        if a or b or c or d:
            return True
        visited.remove((i, j))
        return False
