from typing import List
from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 1

        # Special case for 1
        if 1 in freq:
            if freq[1] % 2 == 0:
                ans = max(ans, freq[1] - 1)
            else:
                ans = max(ans, freq[1])

        for x in freq:
            if x == 1:
                continue

            cur = x
            length = 0

            # Every level except the last needs two copies
            while freq.get(cur, 0) >= 2:
                length += 2
                cur = cur * cur

            # Middle element exists
            if freq.get(cur, 0) >= 1:
                length += 1
            else:
                # Remove one pair because no center exists
                length -= 1

            ans = max(ans, length)

        return ans