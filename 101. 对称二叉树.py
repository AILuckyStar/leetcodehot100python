class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def check(self,left,right):
        if left==None and right==None:
            return True
        elif left==None and right!=None:
            return False
        elif left!=None and right==None:
            return False
        elif left.val!=right.val:
            return False
        else:
            return self.check(left.left,right.right) and self.check(left.right,right.left)
    def isSymmetric(self,root):
        return self.check(root.left,root.right)
