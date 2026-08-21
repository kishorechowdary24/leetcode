from typing import List
from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0

            # Try every subset of coins
            for mask in range(1, 1 << n):
                multiple = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        multiple = lcm(multiple, coins[i])

                        # No multiple of this LCM can be <= x
                        if multiple > x:
                            valid = False
                            break

                if not valid:
                    continue

                amount = x // multiple

                # Odd number of coins -> add
                # Even number of coins -> subtract
                if bits % 2 == 1:
                    total += amount
                else:
                    total -= amount

            return total

        # Binary search for the answer
        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left