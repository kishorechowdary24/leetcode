class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        result = []

        p_count = [0] * 26
        window_count = [0] * 26

        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        left = 0

        for right in range(len(s)):

            window_count[ord(s[right]) - ord('a')] += 1

            if right - left + 1 > len(p):
                window_count[ord(s[left]) - ord('a')] -= 1
                left += 1

            if window_count == p_count:
                result.append(left)

        return result