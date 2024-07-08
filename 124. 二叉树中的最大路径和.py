class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def __init__(self):
        self.res=float('-inf')
    def maxGain(self,root):
        if not root:
            return 0
        left=max(0,self.maxGain(root.left))
        right=max(0,self.maxGain(root.right))
        nodeprice=root.val+left+right
        self.res=max(self.res,nodeprice)
        return root.val+max(left,right)
    def maxPathSum(self,root):
        self.maxGain(root)
        return self.res

