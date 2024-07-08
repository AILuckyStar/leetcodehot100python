import collections


class Solution:
    def orangesRotting(self,grid):
        row, col, time = len(grid), len(grid[0]), 0
        queue = collections.deque()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j))
        while queue:
            l = len(queue)
            for k in range(l):
                i, j = queue.popleft()
                for di, dj in directions:
                    if 0 <= i + di < row and 0 <= j + dj < col and grid[i + di][j + dj] == 1:
                        grid[i + di][j + dj] = 2
                        queue.append((i + di, j + dj))
            if queue:
                time += 1
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        return time



