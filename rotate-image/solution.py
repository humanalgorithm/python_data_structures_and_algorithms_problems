class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        self.print_matrix(matrix)

        for i in range(0, len(matrix)):
            for j in range(i, len(matrix[i])):
                # print "matrix j i {} i j {}".format(matrix[j][i], matrix[i][j])
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                # self.print_matrix(matrix)

        # self.print_matrix(matrix)

        for i in range(0, len(matrix)):
            matrix[i] = matrix[i][::-1]

        return matrix

    def print_matrix(self, matrix):
        print (" ")
        for row in matrix:
            print (row)
        print (" ")

