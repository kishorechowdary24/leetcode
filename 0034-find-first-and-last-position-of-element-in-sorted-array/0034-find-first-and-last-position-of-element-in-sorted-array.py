class Solution(object):

    def findFirst(self, nums, target):
        left = 0
        right = len(nums) - 1
        first = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                first = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return first

    def findLast(self, nums, target):
        left = 0
        right = len(nums) - 1
        last = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                last = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return last

    def searchRange(self, nums, target):
        first = self.findFirst(nums, target)
        last = self.findLast(nums, target)

        return [first, last]