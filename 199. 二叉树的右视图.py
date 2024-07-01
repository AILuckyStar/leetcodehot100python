from collections import deque


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def rightSideView(self,root):
        ans = []
        queue = deque()
        if root == None:
            return ans
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                root = queue.popleft()
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            ans.append(root.val)
        return ans
