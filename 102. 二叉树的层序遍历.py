import collections


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.right=right
        self.left=left

class Solution:
    def levelOrder(self,root):
        queue=collections.deque()
        ans=[]
        if root==None:
            return ans
        queue.append(root)
        while queue:
            res=[]
            size=len(queue)
            while size:
                size-=1
                node=queue.popleft()
                res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(res)
        return ans


