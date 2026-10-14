
class Solution:
    def minEatingSpeed(self, piles, h):
        low, high = 1, max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            if self.canEat(piles, h, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def canEat(self, piles, h, k):
        hours = 0

        for pile in piles:
            hours += (pile + k - 1) // k

        return hours <= h
