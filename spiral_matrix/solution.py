class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        matrix_len = len(matrix) * len(matrix[0])
        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        i, j, char_counter = 0, -1, 0
        solution = []
        while char_counter < matrix_len:
            direction = directions[0]
            next_i, next_j = i + direction[0], j + direction[1]
            if next_i < 0 or next_i >= len(matrix):
                directions.append(directions.pop(0))
            elif next_j < 0 or next_j >= len(matrix[i]):
                directions.append(directions.pop(0))
            elif matrix[next_i][next_j] == "visited":
                directions.append(directions.pop(0))
            else:
                i, j = next_i, next_j
                solution.append(matrix[i][j])
                matrix[i][j] = "visited"
                char_counter += 1
        return solution
