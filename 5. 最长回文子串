class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        dp = [[False] * n for i in range(n)]
        res = s[0]

        for i in range(n):
            dp[i][i] = True
            if i + 1 < n and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                res = s[i:i + 2]
        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and j - i + 1 > len(res):
                    res = s[i:j + 1]
        return res

