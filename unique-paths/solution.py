class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [[1] * n] * m
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

        """"
        unique_paths = {}
        unique_path = []
        last_unique_path = []
        i = 0
        unique_path = True

        while unique_path:
            unique_path = []
            #print "entering with last unique {} unique {}".format(unique_paths, unique_path)
            
            self.search(0, 0, m, n, set(), [], unique_paths, unique_path)
            #print "unique path after"
            #print unique_path
            if unique_path:
                unique_paths[tuple(unique_path)] = []
                unique_paths[tuple(unique_path)].append(unique_path)
        return len(unique_paths.keys())

    def search(self, i, j, m, n, visited, path, existing_paths, unique_path):
        #print visited
        if (i,j) in visited:
            return False

        visited.add((i,j)) 

        if i < 0 or j < 0 or i > m-1 or j > n-1:
            return False
        else:
            path.append((i,j))

        if i == m-1 and j == n-1:
            if existing_paths.get(tuple(path)):
                visited.remove((i,j)) 
                return False
            [unique_path.append(p) for p in path]
            return unique_path

        path_copy = [p for p in path]
        path_2 = self.search(i+1, j, m, n, visited, [p for p in path], existing_paths, unique_path)
        path_1 = self.search(i, j+1, m, n, visited, [p for p in path], existing_paths, unique_path)
        if not path_1 or not path_2:
            path.remove((i,j))
            visited.remove((i,j))

    """
