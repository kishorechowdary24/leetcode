class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:

        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')

            first[idx] = min(first[idx], i)
            last[idx] = i

        intervals = []

        for i in range(26):

            if last[i] == -1:
                continue

            start = first[i]
            end = last[i]

            j = start

            while j <= end:

                idx = ord(s[j]) - ord('a')

                if first[idx] < start:
                    break

                end = max(end, last[idx])

                j += 1

            if j > end:
                intervals.append((start, end))

        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        for start, end in intervals:

            if start > prev_end:
                result.append(s[start:end + 1])
                prev_end = end

        return result