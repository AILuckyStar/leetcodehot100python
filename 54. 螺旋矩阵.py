class Solution:
    def spiralOrder(self,matrix):
        left=0
        right = len(matrix[0])-1
        top = 0
        bottom =len(matrix)-1
        ans = []
        while True:
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top+=1
            if top>bottom:
                break
            for i in  range(top,bottom+1):
                ans.append(matrix[i][right])
            right-=1
            if right<left:
                break
            for i in  range(right,left-1,-1):
                ans.append(matrix[bottom][i])
            bottom-=1
            if bottom<top:
                break
            for i in range(bottom,top-1,-1):
                ans.append(matrix[i][left])
            left+=1
            if left>right:
                break
        return ans
matrix = [[1,2,3],[4,5,6],[7,8,9]]
s=Solution()
print(s.spiralOrder(matrix))

