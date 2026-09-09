class Solution:
    def countCommas(self, n: int) -> int:
        start = 1000
        count = 0
        comma = 1

        while start <= n:
            end = start * 1000 - 1

            if end > n:
                end = n

            count += (end - start + 1) * comma

            start *= 1000
            comma += 1

        return count