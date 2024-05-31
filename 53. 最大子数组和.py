class Solution:
    def maxSubArray(self,nums):
        n=len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        res =0
        for i in range(1,n):
            dp[i]=max(nums[i],dp[i-1]+nums[i])
            res = max(res,dp[i])
        return res

nums = [-2,1,-3,4,-1,2,1,-5,4]
s=Solution()
print(s.maxSubArray(nums))
