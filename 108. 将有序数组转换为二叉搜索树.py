class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def midbuild(self,nums,left,right):
        if left>right:
            return None
        mid=(left+right)//2
        root=TreeNode(nums[mid])
        root.left=self.midbuild(nums,left,mid-1)
        root.right= self.midbuild(nums,mid+1,right)
        return root
    def sortedArrayToBST(self,nums):
        return self.midbuild(nums,0,len(nums)-1)
