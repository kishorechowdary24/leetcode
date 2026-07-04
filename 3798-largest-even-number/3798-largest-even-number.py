class Solution:
    def largestEven(self, s: str) -> str:

        # Traverse from the end to find the last '2'
        for i in range(len(s) - 1, -1, -1):

            if s[i] == '2':
                return s[:i + 1]

        # No '2' found, so no even number is possible
        return ""