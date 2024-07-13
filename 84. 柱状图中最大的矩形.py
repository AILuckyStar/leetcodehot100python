class Solution:
    def largestRectangleArea(self,heights):
        n=len(heights)
        leftindiex,rightindex=[-1]*n,[n]*n#为了第一个和最后一个元素
        stk=[0]
        for i in range(1,n):#右边第一个比当前小
            if heights[i]>=heights[stk[-1]]:
                stk.append(i)
            else:
                while stk and heights[i]<heights[stk[-1]]:
                    rightindex[stk[-1]]=i
                    stk.pop()
                stk.append(i)
        stk=[n-1]
        for i in range(n-2,-1,-1):#左边第一个比当前小
            if heights[i]>=heights[stk[-1]]:
                stk.append(i)
            else:
                while stk and heights[i]<heights[stk[-1]]:
                    leftindiex[stk[-1]]=i
                    stk.pop()
                stk.append(i)
        res=0
        for i in range(n):
            res=max(res,heights[i]*(rightindex[i]-leftindiex[i]-1))
        return res
