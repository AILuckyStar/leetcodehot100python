class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def invertTree(self,root):
        if root==None:
            return root
        stk=[root]
        while stk :
            node=stk.pop()
            if node.left:
                stk.append(node.left)
            if node.right:
                stk.append(node.right)
            node.left,node.right=node.right,node.left
        return root
