class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rootSum(self, root, targetSum):
        if root == None:
            return 0
        res = 0
        if targetSum == root.val:
            res += 1
        res += self.rootSum(root.left, targetSum - root.val) + self.rootSum(root.right, targetSum - root.val)
        return res

    def pathSum(self, root, targetSum):
        if root == None:
            return 0
        ans = 0
        ans += self.rootSum(root, targetSum - root.val)
        ans += self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
        return ans

    
