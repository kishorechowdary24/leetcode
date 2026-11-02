class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mid = len(nums) // 2
        median = nums[mid]
        moves = 0

        for num in nums:
            moves += abs(num - median)
        
        return moves