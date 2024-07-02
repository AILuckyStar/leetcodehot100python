class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recur(self, root, left, right, preorder, inorder, dic):
        if left > right:
            return None
        node = TreeNode(preorder[root])
        mid = dic[preorder[root]]
        node.left = self.recur(root + 1, left, mid - 1,preorder,inorder,dic)
        node.right = self.recur(root + mid - left + 1, mid + 1, right,preorder,inorder,dic)
        return node

    def buildTree(self, preorder, inorder):
        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return self.recur(0,0,len(inorder)-1,preorder,inorder,dic)
