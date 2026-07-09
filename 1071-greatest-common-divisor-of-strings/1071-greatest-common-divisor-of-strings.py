class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        min_len = min(len(str1), len(str2))

        for i in range(min_len, 0, -1):

            candidate = str1[:i]

            if len(str1) % len(candidate) == 0 and len(str2) % len(candidate) == 0:

                if candidate * (len(str1) // len(candidate)) == str1 and \
                   candidate * (len(str2) // len(candidate)) == str2:

                    return candidate

        return ""