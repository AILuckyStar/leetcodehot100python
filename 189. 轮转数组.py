import collections


class Solution:
    def reverse(self,nums,left,right):
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
    def rotate(self,nums,k):
        n=len(nums)
        k=k%len(nums)
        self.reverse(nums,0,n-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)
nums = [1,2,3,4,5,6,7]
k = 3
s=Solution()
s.rotate(nums,k)
print(nums)
