class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()

        maximum = nums[-1]
        moves = 0

        for i in range(len(nums)):
            while nums[i] < maximum:
                nums[i] += 1
                moves += 1

        return moves