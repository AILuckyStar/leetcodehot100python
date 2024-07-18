class Solution:
    def longestValidParentheses(self,s):
        res=0
        n=len(s)
        dp=[0]*n
        for i in range(1,n):
            if s[i]==')':
                if s[i-1]=='(':
                    if i-2>=0:
                        dp[i]=dp[i-2]+2
                    else:
                        dp[i]=2
                else:
                    if i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=='(':
                        if i-dp[i-1]-1-1>=0:
                            dp[i]=dp[i-dp[i-1]-1-1]+dp[i-1]+2
                        else:
                            dp[i]=dp[i-1]+2
                res=max(res,dp[i])
        return res
