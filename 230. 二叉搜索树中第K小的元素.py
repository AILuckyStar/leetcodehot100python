class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res=0
        self.k =0
    def dfs(self,root):
        if root==None:
            return
        self.dfs(root.left)
        if self.k==0:
            return
        self.k-=1
        if self.k==0:
            self.res=root.val
        self.dfs(root.right)
    def kthSmallest(self,root,k):
        self.k=k
        self.dfs(root)
        return  self.res

root = TreeNode(5,
                TreeNode(3, TreeNode(2), TreeNode(4)),
                TreeNode(7, None, TreeNode(8)))


solution = Solution() 

k = 3
solution.kthSmallest(root, k)
print(solution.res)
