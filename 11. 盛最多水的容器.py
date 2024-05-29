class Solution:
    def maxArea(self,height):
        left = 0
        right = len(height)-1
        maxres = 0
        while left<right:
            res = (right-left)*min(height[left],height[right])
            maxres = max(maxres,res)
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return maxres

height = [1,8,6,2,5,4,8,3,7]
s = Solution()
print(s.maxArea(height))
