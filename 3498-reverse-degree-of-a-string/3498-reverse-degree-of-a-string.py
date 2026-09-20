class Solution:
    def reverseDegree(self, s: str) -> int:
        answer = 0

        for i, ch in enumerate(s):
            position = i + 1

            normal_position = ord(ch) - ord('a') + 1

            reverse_position = 27 - normal_position

            answer += reverse_position * position

        return answer