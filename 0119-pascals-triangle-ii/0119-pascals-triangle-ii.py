class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]  # Start with the first row
        
        for i in range(1, rowIndex + 1):
            # Insert 0 at the beginning to help with pairwise addition
            row = [1] + [row[j] + row[j + 1] for j in range(len(row) - 1)] + [1]
        
        return row
