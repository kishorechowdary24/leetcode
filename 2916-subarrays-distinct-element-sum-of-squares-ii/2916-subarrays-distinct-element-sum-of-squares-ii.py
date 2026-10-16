
class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        sumv = [0] * (4 * n)
        sqv = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def update(node, start, end, left, right):
            if left <= start and end <= right:
                length = end - start + 1

                sqv[node] = (
                    sqv[node] + 2 * sumv[node] + length
                ) % MOD

                sumv[node] = (sumv[node] + length) % MOD
                lazy[node] += 1
                return

            mid = (start + end) // 2

            if lazy[node]:
                val = lazy[node]
                left_child = node * 2
                right_child = node * 2 + 1

                left_len = mid - start + 1
                right_len = end - mid

                sqv[left_child] = (
                    sqv[left_child]
                    + 2 * val * sumv[left_child]
                    + val * val * left_len
                ) % MOD

                sumv[left_child] = (
                    sumv[left_child] + val * left_len
                ) % MOD

                sqv[right_child] = (
                    sqv[right_child]
                    + 2 * val * sumv[right_child]
                    + val * val * right_len
                ) % MOD

                sumv[right_child] = (
                    sumv[right_child] + val * right_len
                ) % MOD

                lazy[left_child] += val
                lazy[right_child] += val
                lazy[node] = 0

            if left <= mid:
                update(
                    node * 2, start, mid, left, right
                )

            if right > mid:
                update(
                    node * 2 + 1, mid + 1, end, left, right
                )

            sumv[node] = (
                sumv[node * 2] + sumv[node * 2 + 1]
            ) % MOD

            sqv[node] = (
                sqv[node * 2] + sqv[node * 2 + 1]
            ) % MOD

        last = {}
        ans = 0

        for r, x in enumerate(nums):
            prev = last.get(x, -1)

            update(1, 0, n - 1, prev + 1, r)

            last[x] = r

            ans = (ans + sqv[1]) % MOD

        return ans
