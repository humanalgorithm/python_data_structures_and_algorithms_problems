class Solution(object):
    def numIslands(self, grid):
        self.recursion = 0
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = []
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if self.checkSeenIsland(i, j, islands):
                    continue
                visited_nodes = self.checkIsland(i, j, grid, set())
                if visited_nodes:
                    islands.append(visited_nodes)
        return len(islands)

    def checkSeenIsland(self, i, j, islands):
        for island in islands:
            if (i, j) in island:
                return True
        return False

    def checkIsland(self, i, j, grid, visited_nodes):
        waterLand = self.checkWaterLand(i, j, grid)
        if not waterLand:
            return visited_nodes
        else:
            visited_nodes.add((i, j))

        if (i + 1, j) not in visited_nodes:
            visited_nodes.union(self.checkIsland(i + 1, j, grid, visited_nodes))
        if (i - 1, j) not in visited_nodes:
            visited_nodes.union(self.checkIsland(i - 1, j, grid, visited_nodes))
        if (i, j + 1) not in visited_nodes:
            visited_nodes.union(self.checkIsland(i, j + 1, grid, visited_nodes))
        if (i, j - 1) not in visited_nodes:

            visited_nodes.union(self.checkIsland(i, j - 1, grid, visited_nodes))
        return visited_nodes

    def checkWaterLand(self, i, j, grid):
        out_of_bounds = False
        if i >= len(grid) or i < 0:
            return None
        elif j >= len(grid[i]) or j < 0:
            return None

        if grid[i][j] == "1":
            return (i, j)
        else:
            return None
