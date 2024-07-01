class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.right=right
        self.left=left

class Solution:
    def dfs(self,root,ans):
        if root==None:
            return
        ans.append(root)
        self.dfs(root.left, ans)
        self.dfs(root.right, ans)

    def flatten(self,root):
        ans=[]
        self.dfs(root,ans)
        for i in range(len(ans)-1):
            pre=ans[i]
            cur=ans[i+1]
            pre.right=cur
            pre.left=None

