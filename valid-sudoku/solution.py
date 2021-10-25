from collections import defaultdict
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        trk, r = defaultdict(set), range(9)
        for i in r:
            for j in r:
                e = board[i][j]
                if e == ".":
                    continue
                for k in [(i,), (j), (i//3, j//3)]:
                    if e in trk[k]:
                        return False
                    trk[k].add(e)
        return True
