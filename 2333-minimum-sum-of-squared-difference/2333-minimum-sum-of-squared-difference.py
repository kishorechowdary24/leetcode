from collections import Counter

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]

        k = k1 + k2

        freq = Counter(diff)

        for d in range(max(diff), 0, -1):
            if k == 0:
                break

            count = freq[d]

            if k >= count:
                freq[d - 1] += count
                k -= count
                freq[d] = 0
            else:
                freq[d] -= k
                freq[d - 1] += k
                k = 0
                break

        return sum(count * d * d for d, count in freq.items())