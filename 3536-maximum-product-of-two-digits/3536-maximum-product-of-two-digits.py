class Solution:
    def maxProduct(self, n: int) -> int:
        largest = -1
        seclargest = -1

        while n > 0:
            digit = n % 10
            if digit > largest:
                seclargest = largest
                largest = digit
            elif digit > seclargest:
                seclargest = digit
            
            n //= 10
        return largest * seclargest