class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def lowestCommonAncestor(self,root,p,q):
        if not root or root==p or root==q:
            return root
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        if not left and not right:
            return None
        elif not left:
            return right
        elif not right:
            return left
        else:
            return root
