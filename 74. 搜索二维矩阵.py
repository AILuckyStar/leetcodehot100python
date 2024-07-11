class Solution:
    def searchMatrix(self,matrix,target):
        m=len(matrix)
        n=len(matrix[0])
        row,col=-1,-1
        left,right=0,m-1
        while left<=right:
            mid=(left+right)//2
            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0]>target:
                right=mid-1
            else:
                left=mid+1
        if left==m:
            row=m-1
        else:
            row=right
        left,right=0,n-1
        while left<=right:
            mid = (left+right)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]>target:
                right=mid-1
            else:
                left=mid+1
        return False
