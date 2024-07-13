class Solution:
    def dailyTemperatures(self,temperatures):
        l=len(temperatures)
        ans = [0]*l
        stk=[0]
        for i in range(1,l):
            if temperatures[i]<=temperatures[stk[-1]]:
                stk.append(i)
            else:
                while stk and temperatures[i]>temperatures[stk[-1]]:
                    ans[stk[-1]]=i-stk[-1]
                    stk.pop()
                stk.append(i)#无论栈空了，还是栈顶比当前大了
        return ans
