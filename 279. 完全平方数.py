class Solution:
    def numSquares(self,n):
        dp=[0]*(n+1)
        dp[0]=0
        for i in range(1,n+1):
            minn = float('inf')
            for j in range(1,int(i**0.5)+1):
                minn=min(minn,dp[i-j*j])
            dp[i]=minn+1
        return dp[n]
s=Solution()
print(s.numSquares(12))
