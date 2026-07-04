class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic1 = {}
        for ch in s:
            if ch in dic1:
                dic1[ch] += 1
            else:
                dic1[ch] = 1
        dic2 = {}
        for ch1 in t:
            if ch1 in dic2:
                dic2[ch1] += 1
            else:
                dic2[ch1] = 1
        return dic1 == dic2
        