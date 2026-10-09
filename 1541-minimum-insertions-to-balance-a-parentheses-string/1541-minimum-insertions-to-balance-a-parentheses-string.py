class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                open += 1
            else:
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1
                else:
                    insertions += 1

                if open == 0:
                    insertions += 1
                else:
                    open -= 1

            i += 1

        insertions += 2 * open

        return insertions