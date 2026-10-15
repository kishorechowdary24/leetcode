class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                distinct = len(set(nums[i:j + 1]))

                ans += distinct * distinct

        return ans