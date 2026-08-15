class Solution:
    def longestSubsequence(self, a: List[int]) -> int:
        return any(a) and len(a)-(reduce(xor,a)==0) or 0