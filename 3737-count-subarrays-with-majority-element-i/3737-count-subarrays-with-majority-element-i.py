class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        arr = []
        for num in nums:
            if num == target:
                arr.append(1)
            else:
                arr.append(-1)
        ans = 0
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += arr[j]

                if curr_sum > 0:
                    ans += 1
        return ans