class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def maxDepth(self,root):
        if root==None:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
