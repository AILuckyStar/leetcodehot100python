class Solution:
    def jump(self,nums):
        step=0
        end=0
        nextend=0
        for i in range(len(nums)):
            nextend=max(nextend,i+nums[i])
            if i==end:
                end=min(nextend,len(nums)-1)
                step+=1
        return step
