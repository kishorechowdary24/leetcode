class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        result = []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        # Frequency of words we need
        word_freq = {}

        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        # Try different starting offsets
        for i in range(word_len):

            left = i
            right = i
            count = 0
            current_freq = {}

            while right + word_len <= len(s):

                word = s[right:right + word_len]
                right += word_len

                # Word is not present in words
                if word not in word_freq:
                    current_freq = {}
                    count = 0
                    left = right
                    continue

                # Add word to current window
                current_freq[word] = current_freq.get(word, 0) + 1
                count += 1

                # Too many occurrences of this word
                while current_freq[word] > word_freq[word]:
                    left_word = s[left:left + word_len]
                    current_freq[left_word] -= 1
                    left += word_len
                    count -= 1

                # We have all the required words
                if count == word_count:
                    result.append(left)

        return result