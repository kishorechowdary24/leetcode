class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mmp = {}
        for num in nums:
            if num in  mmp:
                mmp[num] += 1
            else:
                mmp[num] = 1
        ans = []
        target = len(nums) // 3
        for key, value in mmp.items():
            if value > target:
                ans.append(key)

        return ans