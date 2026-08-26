class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        left = 0
        ones = 0

        ans = ""
        min_length = float('inf')

        for right in range(len(s)):

            if s[right] == '1':
                ones += 1

            while ones == k:

                current_length = right - left + 1
                current = s[left:right + 1]

                if current_length < min_length or (current_length == min_length and current < ans):
                    ans = current
                    min_length = current_length

                if s[left] == '1':
                    ones -= 1

                left += 1

        return ans