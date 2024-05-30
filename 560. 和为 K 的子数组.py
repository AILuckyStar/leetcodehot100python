import collections


class Solution:
    def subarraySum(self,nums,k):
        mp = collections.defaultdict(int)
        mp[0]=1
        presum=0
        res=0
        n=len(nums)
        for i in range(n):
            presum+=nums[i]
            if presum-k in mp:
                res+=mp[presum-k]
            mp[presum]+=1
        return res

nums = [1,1,1]
k = 2
s = Solution()
print(s.subarraySum(nums,k))
