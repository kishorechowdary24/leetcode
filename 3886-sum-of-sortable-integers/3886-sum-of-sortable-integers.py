class Solution(object):
    def sortableIntegers(self, nums):
        n = len(nums)
        sorted_nums = sorted(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for start in range(0, n, k):
                block = nums[start:start + k]
                target = sorted_nums[start:start + k]

                if sorted(block) != target:
                    valid = False
                    break

                m = len(block)
                descents = sum(
                    block[i] > block[(i + 1) % m]
                    for i in range(m)
                )

                if descents > 1:
                    valid = False
                    break

            if valid:
                ans += k

        return ans
