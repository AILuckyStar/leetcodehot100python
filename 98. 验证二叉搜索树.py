class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def helper(self,root):
        pre=float('-inf')
        stack=[]
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            node=stack.pop()
            if node.val <= pre:
                return False
            pre=node.val
            root=node.right
        return True



    def isValidBSF(self,root):
        return self.helper(root)
