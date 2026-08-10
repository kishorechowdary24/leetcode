class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_C = 0
        for num in nums:
            if num == 1:
                count += 1
                max_C = max(max_C, count)
            else:
                count = 0
            
        return max_C