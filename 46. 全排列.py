class Solution:
    def backtracking(self,nums,path,used,res):
        if len(path)==len(nums):
            res.append(path.copy())
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i]=True
            path.append(nums[i])
            self.backtracking(nums,path,used,res)
            path.pop()
            used[i]=False
    def permute(self,nums):
        res=[]
        path=[]
        used=[False]*len(nums)
        self.backtracking(nums,path,used,res)
        return res
