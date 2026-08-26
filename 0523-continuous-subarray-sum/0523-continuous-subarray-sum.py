class Solution:
    def checkSubarraySum(self, nums, k):
        remainder_map = {0: -1}
        prefixsum = 0

        for i in range(len(nums)):
            prefixsum += nums[i]

            remainder = prefixsum % k

            if remainder in remainder_map:
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                remainder_map[remainder] = i

        return False