class Solution:
    def rob(self, nums: list[int]) -> int:
        prev2 = 0
        prev1 = 0

        for money in nums:
            take = money + prev2
            skip = prev1

            current = max(take, skip)

            prev2 = prev1
            prev1 = current
        return prev1