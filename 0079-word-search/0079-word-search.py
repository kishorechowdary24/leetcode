class Solution:
    def exist(self, board, word):

        rows = len(board)
        cols = len(board[0])

        def dfs(i, j, index):

            if index == len(word):
                return True

            # Boundary check
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False

            if board[i][j] != word[index]:
                return False

            temp = board[i][j]

            board[i][j] = "$"

            found = (
                dfs(i, j + 1, index + 1) or   # Right
                dfs(i, j - 1, index + 1) or   # Left
                dfs(i + 1, j, index + 1) or   # Down
                dfs(i - 1, j, index + 1)      # Up
            )

            board[i][j] = temp

            return found

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False