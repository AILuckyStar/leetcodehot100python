class Solution:
    def canJump(self,nums):
        end=0
        for i in range(len(nums)):
            if i >end:
                return False
            end=max(end,i+nums[i])
        return True
