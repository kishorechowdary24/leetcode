class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        count = {}
        for row in grid:
            for num in row:
                if num in count:
                    count[num] += 1
                else:
                    count[num] = 1

        n = len(grid)
        repeated = 0
        missing = 0
        for i in range(1, n*n + 1):
             if count.get(i, 0) == 2:
                repeated = i
             elif count.get(i, 0) == 0:
                missing = i
        return [repeated, missing]
