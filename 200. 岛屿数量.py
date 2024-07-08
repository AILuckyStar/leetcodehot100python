class Solution:
    def dfs(self,grid,i,j):
        if not 0<=i<len(grid) or not 0<=j<len(grid[0]) or grid[i][j]=='0':
            return
        grid[i][j]='0'
        self.dfs(grid,i-1,j)
        self.dfs(grid,i+1,j)
        self.dfs(grid,i,j-1)
        self.dfs(grid,i,j+1)
    def numIslands(self,grid):
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    self.dfs(grid,i,j)
                    res+=1
        return res
