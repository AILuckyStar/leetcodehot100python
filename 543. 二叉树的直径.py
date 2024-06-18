class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def __init__(self):
        self.ans=0
    def depth(self,root):
        if root==None:
            return 0
        L =self.depth(root.left)
        R= self.depth(root.right)
        self.ans=max(self.ans,L+R+1)
        return max(L,R)+1
    def diameterOfBinaryTree(self,root):
        self.depth(root)
        return self.ans-1
