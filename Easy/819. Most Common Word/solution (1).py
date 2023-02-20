# 819. Most Common Word


from collections import Counter

class Solution:
    # String Processing in Pipeline
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        normalized_str = "".join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        words = normalized_str.split()

        counts = Counter(words)
        banned_words = set(banned)
        for word in counts.keys():
            if word in banned_words:
                counts[word] = 0

        return max(counts.items(), key=lambda p: p[1])[0]