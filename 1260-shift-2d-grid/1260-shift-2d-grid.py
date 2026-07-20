class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        rows = len(grid)
        cols = len(grid[0])

        total = rows * cols

        k %= total

        ans = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):

                current = i * cols + j

                new = (current + k) % total

                newRow = new // cols
                newCol = new % cols

                ans[newRow][newCol] = grid[i][j]

        return ans