class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        ans = []

        for num, count in sorted_freq[:k]:
            ans.append(num)

        return ans