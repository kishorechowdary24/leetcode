class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0

        freq = {0: 1}

        for num in nums:
            prefix += num

            need = prefix - k

            if need in freq:
                count += freq[need]

            freq[prefix] = freq.get(prefix, 0) + 1

        return count