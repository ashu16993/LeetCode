'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

'''

class Solution:
    def check_island(self,grid,i,j,visited):
        flag = 0
        # print(i,j)
        visited[i][j]=1
        if grid[i][j]=="0":
            return 1
        else:
            up = 1
            down = 1
            left = 1
            right = 1
            if i>0 and visited[i-1][j]==0:
                up = self.check_island(grid,i-1,j,visited)
            if i<len(grid)-1 and visited[i+1][j]==0:
                down = self.check_island(grid,i+1,j,visited)
            
            if j<len(grid[0])-1 and visited[i][j+1]==0:
                left = self.check_island(grid,i,j+1,visited)
            if j>0 and visited[i][j-1]==0:
                right = self.check_island(grid,i,j-1,visited)
            
            flag = (up | down | left |right)
        
        return flag
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # print(grid)
        islands = 0
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=="1":
                    if visited[i][j]!=1:
                        islands+=self.check_island(grid,i,j,visited)
                else:
                    visited[i][j]=1
        return islands



print(Solution().numIslands([["1","0","1","1","0"],["1","1","0","0","0"],["1","1","0","0","1"],["0","0","0","0","1"]]))