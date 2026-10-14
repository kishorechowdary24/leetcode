class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """

        if sum > 9 * num:
            return ""

        result = []
        remaining = sum

        for i in range(num):
            digit = min(9, remaining)
            result.append(str(digit))
            remaining -= digit

        return "".join(result)