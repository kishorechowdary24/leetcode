class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_array = sorted(set(arr))
        rank = {}

        for i in range(len(sorted_array)):
            rank[sorted_array[i]] = i + 1
        ans = []

        for i in range(len(arr)):
            ans.append(rank[arr[i]])
        return ans