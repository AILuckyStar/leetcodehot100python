class Solution:
    def climbStairs(self, n: int) -> int:
        f1=1
        if n<=1:
            return f1
        f2=2
        for i in range(3,n+1):
            f1=f1+f2
            f2,f1=f1,f2
        return f2
