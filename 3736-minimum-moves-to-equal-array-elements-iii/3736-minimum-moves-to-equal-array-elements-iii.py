class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxinum = max(nums)
        moves = 0
        for num in nums:
            moves += maxinum - num
        return moves