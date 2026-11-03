class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1 
            else:
                freq[ch] = 1
        sort_char = sorted(freq, key = freq.get, reverse =True)
        result = ""

        for ch in sort_char:
            result += ch * freq[ch]
        return result
