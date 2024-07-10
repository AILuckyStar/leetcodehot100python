class Solution:
    def backtrack(self,res,path,s):
        if len(s)==0:
            res.append(path.copy())
            return
        for i in range(1,len(s)+1):
            pre=s[0:i]
            if pre==pre[::-1]:
                path.append(pre)
                self.backtrack(res,path,s[i:])
                path.pop()
    def partition(self,s):
        res=[]
        self.backtrack(res,[],s)
        return res

Sol=Solution()
print(Sol.partition('aab'))
