# 151. Reverse Words in a String

# Runtime: 40 ms, faster than 55.52% of Python3 online submissions for Reverse Words in a String.

# Memory Usage: 14.3 MB, less than 67.77% of Python3 online submissions for Reverse Words in a String.


from collections import deque

class Solution:
    # Deque of Words
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1
        # Remove leading spaces.
        while left <= right and s[left] == " ":
            left += 1

        # Remove trailing spaces.
        while left <= right and s[right] == " ":
            right -= 1

        deq, word = deque(), []
        # Push word by word in front of deque.
        while left <= right:
            if s[left] == " " and word:
                deq.appendleft("".join(word))
                word = []
            elif s[left] != " ":
                word.append(s[left])
            left += 1
        deq.appendleft("".join(word))

        return " ".join(deq)