class Solution:
    def findDuplicate(self,nums):
        left,right=1,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            cnt=0
            for i in range(len((nums))):
                if nums[i]<=mid:
                    cnt+=1
            if cnt<=mid:
                left=mid+1
            else:
                right=mid-1
                ans=mid
        return ans
