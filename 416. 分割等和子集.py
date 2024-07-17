class Solution:
    def canPartition(self,nums):
        n=len(nums)
        if n<2:
            return False
        total=sum(nums)
        maxNum=max(nums)
        if total%2==1:
            return False
        target=total//2
        if maxNum>target:
            return False
        dp=[[False]*(target+1) for _ in range(n)]
        for i in range(n):
            dp[i][0]=True
        dp[0][nums[0]]=True
        for i in range(n):
            for j in range(1,target+1):
                if nums[i]<=target:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n-1][target]
