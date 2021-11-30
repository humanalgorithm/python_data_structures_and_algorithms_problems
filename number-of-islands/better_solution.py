class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        island_set, island_count = set(), 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                island = set()
                self.searchIsland(i, j, grid, island, set(), island_set)
                island_count = island_count + 1 if island else island_count
                [island_set.add(val) for val in island]
        return island_count

    def searchIsland(self, i, j, grid, island, visited, island_set):
        if (i, j) in visited or (i, j) in island_set:
            return

        visited.add((i, j))
        if i < 0 or i > len(grid) - 1:
            return
        if j < 0 or j > len(grid[i]) - 1:
            return
        if grid[i][j] == "0":
            return
        if grid[i][j] == "1":
            island.add((i, j))

        self.searchIsland(i + 1, j, grid, island, visited, island_set)
        self.searchIsland(i - 1, j, grid, island, visited, island_set)
        self.searchIsland(i, j + 1, grid, island, visited, island_set)
        self.searchIsland(i, j - 1, grid, island, visited, island_set)
