# 5. Longest Palindromic Substring

# Time Limit Exceeded


class Solution:
    # Dynamic Programming
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        # `pal[i][j]` is true if the substring `s[i:j + 1]` is a palindrome.
        pal = [[False] * len(s) for _ in range(len(s))]

        ans = s[0]
        for n in range(1, len(s) + 1):
            for i in range(len(s) - n + 1):
                if n == 1:
                    pal[i][i] = True
                elif n == 2:
                    pal[i][i + 1] = s[i] == s[i + 1]
                    if pal[i][i + 1]:
                        ans = s[i:i + 2]
                else:
                    j = i + n - 1
                    pal[i][j] = pal[i + 1][j - 1] and s[i] == s[j]
                    if pal[i][j] and j - i + 1 > len(ans):
                        ans = s[i:j + 1]

        return ans