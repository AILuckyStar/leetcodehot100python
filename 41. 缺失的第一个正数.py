class Solution:
    def firstMissingPositive(self,nums):
        n=len(nums)
        for i in range(n):
            if nums[i]<=0:
                nums[i] = n+1
        for i in range(n):
            if abs(nums[i])<n+1:
                x=abs(nums[i])
                nums[x-1] = -abs(nums[x-1])
        for i in range(n):
            if nums[i]>0:
                return i+1
        return n+1
s=Solution()
print(s.firstMissingPositive(nums = [7,8,9,11,12]))
