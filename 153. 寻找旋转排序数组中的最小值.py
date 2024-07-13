class Solution:
    def findMin(self,nums):
        left,right=0,len(nums)-1
        if nums[0]<nums[len(nums)-1]:
            return nums[0]
        if nums[len(nums)-1]<nums[len(nums)-2]:
            return nums[-1]
        while left<=right:
            mid=(left+right)//2
            if nums[mid-1]>nums[mid] and nums[mid]<nums[mid+1]:
                return nums[mid]
            else:
                if nums[mid]>=nums[0]:
                    left=mid+1
                else:
                    right=mid-1
        return -1
#题解大都用开区间，为保证笔者不混乱，还是用闭区间，麻烦一点
