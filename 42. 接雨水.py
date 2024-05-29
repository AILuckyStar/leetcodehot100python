class Solution:
    def trap(self,height):
        if not height:
            return 0
        n = len(height)
        leftMax = [0]*n
        leftMax[0]=height[0]
        rightMax = [0]*n
        rightMax[n-1]=height[n-1]
        for i in range(1,n):
            leftMax[i]=max(leftMax[i-1],height[i])
        for i in range(n-2,-1,-1):
            rightMax[i]=max(rightMax[i+1],height[i])
        res = 0
        for i in range(n):
            res+=min(leftMax[i],rightMax[i])-height[i]
        return  res
height = [0,1,0,2,1,0,1,3,2,1,2,1]
s=Solution()
print(s.trap(height))
