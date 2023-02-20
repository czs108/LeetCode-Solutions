# 819. Most Common Word

# Runtime: 68 ms, faster than 5.28% of Python3 online submissions for Most Common Word.

# Memory Usage: 14.1 MB, less than 98.43% of Python3 online submissions for Most Common Word.


from collections import Counter

class Solution:
    # Character Processing in One-Pass
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        counts = Counter()
        banned_words = set(banned)

        word_buffer = []
        for i, c in enumerate(paragraph):
            if c.isalnum():
                word_buffer.append(c.lower())
                if i != len(paragraph) - 1:
                    continue
            if word_buffer:
                word = "".join(word_buffer)
                if word not in banned_words:
                    counts[word] += 1
                word_buffer = []
        return max(counts.items(), key=lambda p: p[1])[0]