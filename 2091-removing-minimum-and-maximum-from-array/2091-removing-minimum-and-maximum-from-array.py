class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        minnum = nums[0]
        maxnum = nums[0]

        minIndex = 0
        maxIndex = 0

        for i in range(1, n):
            if nums[i] < minnum:
                minnum = nums[i]
                minIndex = i

            if nums[i] > maxnum:
                maxnum = nums[i]
                maxIndex = i

        a = min(minIndex, maxIndex)
        b = max(minIndex, maxIndex)

        front = b + 1

        back = n - a

        both = (a + 1) + (n - b)

        return min(front, min(back,both))