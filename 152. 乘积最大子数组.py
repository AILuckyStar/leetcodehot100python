class Solution:
    def maxProduct(self,nums):
        n=len(nums)
        minf=[0]*n
        maxf=[0]*n
        minf[0]=nums[0]
        maxf[0]=nums[0]
        res=nums[0]
        for i in range(1,n):
            maxf[i]=max(maxf[i-1]*nums[i],max(minf[i-1]*nums[i],nums[i]))
            minf[i]=min(maxf[i-1]*nums[i],min(minf[i-1]*nums[i],nums[i]))
            res=max(res,maxf[i])
        return res
