class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        stack = [("", 0, 0)]

        while stack:
            current, open, close = stack.pop()

            if open == n and close == n:
                result.append(current)
                continue

            if open < n:
                stack.append((current + "(", open + 1, close))

            if close < open:
                stack.append((current + ")", open, close + 1))

        return result