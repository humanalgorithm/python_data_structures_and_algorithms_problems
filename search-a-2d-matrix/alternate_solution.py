class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        c_rows = []
        for index, row in enumerate(matrix):
            if row[0] <= target <= row[-1]:
                c_rows.append(index)
        if not c_rows:
            return False

        matrix_filtered = matrix[c_rows[0]: c_rows[-1] + 1]
        for x in range(0, len(matrix[0])):
            col_set = set()
            [col_set.add(row[x]) for row in matrix_filtered]
            if target in col_set:
                return True
        return False
