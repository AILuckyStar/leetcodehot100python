class Solution:
    def threeSum(self,nums):
        n=len(nums)
        nums.sort()
        ans = list()
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            k=n-1
            j=i+1
            while j<k:
                if j>i+1 and nums[j]==nums[j-1]:
                    j+=1
                    continue
                if k <n-1 and nums[k]==nums[k+1]:
                    k-=1
                    continue
                if nums[i]+nums[j]+nums[k] == 0:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                elif nums[i]+nums[j]+nums[k] > 0:
                    k-=1
                else:
                    j+=1
        return ans

# nums = [-1,0,1,2,-1,-4]
nums = [-5,0,0,0,1,1,2,2,4]
s =Solution()
print(s.threeSum(nums))


