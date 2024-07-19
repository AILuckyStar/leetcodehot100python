class Solution:
    def sortColors(self,nums):
        ptr=0
        for i in range(len(nums)):
            if nums[i]==0:
                nums[ptr],nums[i]=nums[i],nums[ptr]
                ptr+=1
        for i in range(ptr,len(nums)):
            if nums[i]==1:
                nums[ptr],nums[i]=nums[i],nums[ptr]
                ptr+=1
        return nums
nums=[2,0,2,1,1,0]
s=Solution()
print(s.sortColors(nums))
