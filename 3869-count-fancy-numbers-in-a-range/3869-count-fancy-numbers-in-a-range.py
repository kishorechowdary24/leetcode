from functools import lru_cache

class Solution:
    def countFancy(self, l: int, r: int) -> int:

        def is_good(x):
            s = str(x)
            if len(s) == 1:
                return True

            inc = True
            dec = True

            for i in range(1, len(s)):
                if s[i] <= s[i - 1]:
                    inc = False
                if s[i] >= s[i - 1]:
                    dec = False

            return inc or dec

        def solve(num):
            if num < 0:
                return 0

            digits = list(map(int, str(num)))
            n = len(digits)

            @lru_cache(None)
            def dp(pos, prev, started, tight, state, digit_sum):
                """
                state:
                0 -> direction not decided
                1 -> increasing
                2 -> decreasing
                3 -> invalid
                """

                if pos == n:
                    if not started:
                        return 0

                    if state != 3:
                        return 1

                    return 1 if is_good(digit_sum) else 0

                limit = digits[pos] if tight else 9
                ans = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started:
                        if d == 0:
                            ans += dp(
                                pos + 1,
                                0,
                                False,
                                ntight,
                                0,
                                0
                            )
                        else:
                            ans += dp(
                                pos + 1,
                                d,
                                True,
                                ntight,
                                0,
                                d
                            )
                    else:
                        if state == 3:
                            ns = 3

                        elif state == 0:
                            if d > prev:
                                ns = 1
                            elif d < prev:
                                ns = 2
                            else:
                                ns = 3

                        elif state == 1:
                            ns = 1 if d > prev else 3

                        else:
                            ns = 2 if d < prev else 3

                        ans += dp(
                            pos + 1,
                            d,
                            True,
                            ntight,
                            ns,
                            digit_sum + d
                        )

                return ans

            return dp(0, 0, False, True, 0, 0)

        return solve(r) - solve(l - 1)