class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_s = ""
        for ch in s:
            if ch.isalnum():
                new_s += ch.lower()


        def helper(i,j):
            if i >= j:
                return True
            
            if new_s[i] != new_s[j]:
                return False
            
            return helper(i+1, j-1)
        return helper(0, len(new_s)-1)
