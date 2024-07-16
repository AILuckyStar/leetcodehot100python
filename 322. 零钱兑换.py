class Solution:
    def coinChange(self,coins,amount):
        dp=[-1]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            minn=float('inf')
            for coin in coins:
                if i-coin>=0 and dp[i-coin]!=-1:
                    minn=min(minn,dp[i-coin]+1)
                dp[i]=minn if minn != float('inf') else -1
        return dp[amount] if dp[amount]!=-1 else -1
