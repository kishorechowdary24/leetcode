class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        count = 1
        longest = 1
        lastsmaller = nums[0]

        for i in range(1, len(nums)):
            if nums[i] - 1 == lastsmaller:
                count += 1
                lastsmaller = nums[i]

            elif nums[i] != lastsmaller:
                count = 1
                lastsmaller = nums[i]

            longest = max(longest, count)

        return longest