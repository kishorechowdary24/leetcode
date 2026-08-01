class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def solve(i, j):

            if i == j:
                return nums[i]

            left = nums[i] - solve(i + 1, j)

            right = nums[j] - solve(i, j - 1)

            return max(left, right)

        return solve(0, len(nums) - 1) >= 0