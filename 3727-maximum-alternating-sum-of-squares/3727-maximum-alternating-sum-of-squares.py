
class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        squares = []

        for num in nums:
            squares.append(num * num)

        squares.sort(reverse=True)

        positive_count = (len(nums) + 1) // 2

        answer = sum(squares[:positive_count]) - sum(squares[positive_count:])

        return answer
