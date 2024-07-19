class Solution:
    def reverse(self,nums,i,j):
        left,right=i,j
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
    def nextPermutation(self,nums):
        for i in range(len(nums)-1,-1,-1):
            for j in range(len(nums)-1,i,-1):
                if nums[i]<nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
                    self.reverse(nums,i+1,len(nums)-1)
                    return
        self.reverse(nums,0,len(nums)-1)
