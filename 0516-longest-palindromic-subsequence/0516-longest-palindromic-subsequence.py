class Solution:
    def longestPalindromeSubseq(self, s: str):

        memo = {}

        def dfs(left, right):

            if left > right:
                return 0

            if left == right:
                return 1

            if (left, right) in memo:
                return memo[(left, right)]

            if s[left] == s[right]:
                memo[(left, right)] = 2 + dfs(left + 1, right - 1)
            else:
                memo[(left, right)] = max(
                    dfs(left + 1, right),
                    dfs(left, right - 1)
                )

            return memo[(left, right)]

        return dfs(0, len(s) - 1)