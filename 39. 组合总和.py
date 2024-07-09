class Solution:
    def backtracking(self,res,ans,candiates,target):
        if target<0 or len(candiates)==0:
            return
        if target==0:
            res.append(ans.copy())
            return
        ans.append(candiates[0])
        self.backtracking(res,ans,candiates,target-candiates[0])
        ans.pop()
        self.backtracking(res,ans,candiates[1:],target)

    def combinationSum(self,candidates,target):
        res=[]
        self.backtracking(res,[],candidates,target)
        return res
