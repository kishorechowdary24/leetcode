class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:

        n = len(nums)

        for i in range(n):

            maxi = nums[0]

            for j in range(i + 1):
                maxi = max(maxi, nums[j])

            mini = nums[i]

            for j in range(i, n):
                mini = min(mini, nums[j])

            score = maxi - mini

            if score <= k:
                return i

        return -1