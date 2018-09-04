'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.

'''



class Solution(object):
    
   def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])
        max_area = 0
        seen = set()
        stack = []
        
        # Iterate through grid and run DFS
        for row in range(M):
            for col in range(N):
                # Run a DFS from nodes that are islands and are not seen yet
                if grid[row][col] and (row, col) not in seen:
                    stack.append((row, col))
                    seen.add((row, col))
                    area = 0
                    
                    # Run a DFS using a stack. Stack invariant: all nodes in stack are marked as seen so we
                    # will never consider a duplicate solution and double add to area.
                    while stack:
                        point = stack.pop()
                        area += 1

                        # Add neighbors that are valid and not seen yet to stack and seen set
                        # (1) Bottom
                        if point[0] > 0 and grid[point[0]-1][point[1]] and (point[0]-1, point[1]) not in seen:
                            stack.append((point[0]-1, point[1]))
                            seen.add((point[0]-1, point[1]))
                        # (2) Top
                        if point[0] < M - 1 and grid[point[0]+1][point[1]] and (point[0]+1, point[1]) not in seen:
                            stack.append((point[0]+1, point[1]))
                            seen.add((point[0]+1, point[1]))
                        # (3) Left
                        if point[1] > 0 and grid[point[0]][point[1]-1] and (point[0], point[1]-1) not in seen:
                            stack.append((point[0], point[1]-1))
                            seen.add((point[0], point[1]-1))
                        # (4) Right
                        if point[1] < N - 1 and grid[point[0]][point[1]+1] and (point[0], point[1]+1) not in seen:
                            stack.append((point[0], point[1]+1))
                            seen.add((point[0], point[1]+1))

                    max_area = max(max_area, area)
        
        return max_area 