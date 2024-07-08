class Solution:
    def dfs(self,nums,level,path,res):
        if level==len(nums):
            res.append(path.copy())
            return
        path.append(nums[level])
        self.dfs(nums,level+1,path,res)
        path.pop()
        self.dfs(nums,level+1,path,res)
    def subsets(self,nums):
        res=[]
        path=[]
        self.dfs(nums,0,path,res)
        return res
