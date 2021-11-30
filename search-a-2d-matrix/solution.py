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
        for row in matrix_filtered:
            if self.binary_search(row, target):
                return True
        return False

    def binary_search(self, row, target):
        l, r = 0, len(row) - 1
        while l <= r:
            mid = l + (r - l) / 2
            if row[mid] == target:
                return True
            if row[l] <= target <= row[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return False
