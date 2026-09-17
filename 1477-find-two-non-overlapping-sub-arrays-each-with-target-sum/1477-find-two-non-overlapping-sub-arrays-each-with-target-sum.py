class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:

        n = len(arr)

        INF = float('inf')

        dp = [INF] * n

        left = 0
        curr_sum = 0

        ans = INF

        for right in range(n):

            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if right > 0:
                dp[right] = dp[right - 1]

            if curr_sum == target:

                length = right - left + 1

                if left > 0 and dp[left - 1] != INF:
                    ans = min(ans, dp[left - 1] + length)

                dp[right] = min(dp[right], length)

        return -1 if ans == INF else ans