import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        small = []  # Max heap
        large = []  # Min heap

        delayed = set()
        side = {}

        small_sum = 0
        large_sum = 0

        small_size = 0
        large_size = 0

        def prune(heap):
            while heap and heap[0][1] in delayed:
                _, idx = heapq.heappop(heap)
                delayed.remove(idx)

        def rebalance():
            nonlocal small_size, large_size
            nonlocal small_sum, large_sum

            target = (small_size + large_size + 1) // 2

            prune(small)
            prune(large)

            while small_size > target:
                neg_value, idx = heapq.heappop(small)
                value = -neg_value

                small_size -= 1
                large_size += 1

                small_sum -= value
                large_sum += value

                side[idx] = "large"
                heapq.heappush(large, (value, idx))
                prune(small)

            while small_size < target:
                prune(large)

                value, idx = heapq.heappop(large)

                large_size -= 1
                small_size += 1

                large_sum -= value
                small_sum += value

                side[idx] = "small"
                heapq.heappush(small, (-value, idx))
                prune(large)

        def add(idx):
            nonlocal small_size, large_size
            nonlocal small_sum, large_sum

            value = nums[idx]

            prune(small)

            if not small or value <= -small[0][0]:
                heapq.heappush(small, (-value, idx))
                small_size += 1
                small_sum += value
                side[idx] = "small"
            else:
                heapq.heappush(large, (value, idx))
                large_size += 1
                large_sum += value
                side[idx] = "large"

            rebalance()

        def remove(idx):
            nonlocal small_size, large_size
            nonlocal small_sum, large_sum

            value = nums[idx]
            delayed.add(idx)

            if side[idx] == "small":
                small_size -= 1
                small_sum -= value
            else:
                large_size -= 1
                large_sum -= value

            del side[idx]

            prune(small)
            prune(large)
            rebalance()

        def get_cost():
            prune(small)

            median = -small[0][0]

            left_cost = median * small_size - small_sum
            right_cost = large_sum - median * large_size

            return left_cost + right_cost

        # Calculate every window's cost
        costs = []

        for i in range(n):
            add(i)

            if i >= x:
                remove(i - x)

            if i >= x - 1:
                costs.append(get_cost())

        # Dynamic programming
        INF = float('inf')

        dp = [[INF] * (n + 1) for _ in range(k + 1)]

        for i in range(n + 1):
            dp[0][i] = 0

        for j in range(1, k + 1):
            for i in range(x, n + 1):
                dp[j][i] = dp[j][i - 1]

                window_cost = costs[i - x]
                previous = dp[j - 1][i - x]

                dp[j][i] = min(
                    dp[j][i],
                    previous + window_cost
                )

        return dp[k][n]