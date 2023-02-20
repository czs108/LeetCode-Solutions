# 5. Longest Palindromic Substring

# Time Limit Exceeded


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        # `pal[i][j]` is true if the substring `s[i:j + 1]` is a palindrome.
        pal = [[False] * len(s) for _ in range(len(s))]

        ans = s[0]
        for i in range(len(s)):
            pal[i][i] = True
        for i in range(len(s) - 1):
            pal[i + 1][i] = pal[i][i + 1] = s[i] == s[i + 1]
            if pal[i][i + 1]:
                ans = s[i:i + 2]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                pal[j][i] = pal[i][j] = pal[i][j] = pal[i + 1][j - 1] and s[i] == s[j]
                if pal[i][j] and j - i + 1 > len(ans):
                    ans = s[i:j + 1]

        return ans