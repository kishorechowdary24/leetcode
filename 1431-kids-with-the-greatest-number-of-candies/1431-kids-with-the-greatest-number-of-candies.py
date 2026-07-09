class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        ans = []

        for i in range(len(candies)):
            new_candy = candies[i] + extraCandies

            if new_candy >= max_candy:
                ans.append(True)
            else:
                ans.append(False)

        return ans