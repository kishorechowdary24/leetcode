from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Fill the sets with existing numbers
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    box = (r // 3) * 3 + (c // 3)
                    boxes[box].add(board[r][c])

        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        box = (r // 3) * 3 + (c // 3)

                        for ch in "123456789":
                            if (ch not in rows[r] and
                                ch not in cols[c] and
                                ch not in boxes[box]):

                                # Place the number
                                board[r][c] = ch
                                rows[r].add(ch)
                                cols[c].add(ch)
                                boxes[box].add(ch)

                                if solve():
                                    return True

                                # Backtrack
                                board[r][c] = "."
                                rows[r].remove(ch)
                                cols[c].remove(ch)
                                boxes[box].remove(ch)

                        return False

            return True

        solve()