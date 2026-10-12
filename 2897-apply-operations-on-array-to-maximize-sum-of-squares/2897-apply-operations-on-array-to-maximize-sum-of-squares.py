class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        bits = [0] * 31

        for num in nums:
            for bit in range(31):
                if num & (1 << bit):
                    bits[bit] += 1

        ans = [0] * k

        for bit in range(30, -1, -1):
            count = bits[bit]

            for i in range(min(count, k)):
                ans[i] |= (1 << bit)

        total = 0

        for num in ans:
            total += num * num

        return total % (10**9 + 7)