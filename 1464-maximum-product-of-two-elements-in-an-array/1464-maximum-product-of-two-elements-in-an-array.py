class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = 0
        s_largest = 0

        for num in nums:
            if num > largest:
                s_largest = largest
                largest = num
            elif num > s_largest:
                s_largest = num
        return (largest - 1) * (s_largest - 1)