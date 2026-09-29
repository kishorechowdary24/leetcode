class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        path_length = m + n - 1
        if path_length % 2 == 1:
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    previous_balances = {0}
                else:
                    previous_balances = set()

                    if i > 0:
                        previous_balances.update(dp[i - 1][j])

                    if j > 0:
                        previous_balances.update(dp[i][j - 1])

                change = 1 if grid[i][j] == "(" else -1

                for balance in previous_balances:
                    new_balance = balance + change
                    if new_balance >= 0:
                        dp[i][j].add(new_balance)

        return 0 in dp[m - 1][n - 1]