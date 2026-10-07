class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        res = set()

        def is_valid(string):
            count = 0
            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        def backtrack(index, path, left, right, removals):
            if index == len(s):
                if left == 0 and right == 0 and is_valid(path):
                    res.add(path)
                return

            ch = s[index]

            if ch == '(' and left > 0:
                backtrack(index + 1, path, left - 1, right, removals - 1)

            if ch == ')' and right > 0:
                backtrack(index + 1, path, left, right - 1, removals - 1)

            backtrack(index + 1, path + ch, left, right, removals)

        left = right = 0

        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        backtrack(0, "", left, right, left + right)

        return list(res)