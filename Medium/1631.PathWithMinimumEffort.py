'''
    You are a hiker preparing for an upcoming hike. You are 
    given heights, a 2D array of size rows x columns, where 
    heights[row][col] represents the height of cell (row, col). 
    You are situated in the top-left cell, (0, 0), and you 
    hope to travel to the bottom-right cell, 
    (rows-1, columns-1) (i.e., 0-indexed). You can move up, 
    down, left, or right, and you wish to find a route that 
    requires the minimum effort.

    A route's effort is the maximum absolute difference in 
    heights between two consecutive cells of the route.

    Return the minimum effort required to travel from the 
    top-left cell to the bottom-right cell.

    Example:
            [1,2,2]
            [3,8,2]
            [5,3,5]
    Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
    Output: 2
    Explanation: The route of [1,3,5,3,5] has a maximum 
                 absolute difference of 2 in consecutive 
                 cells.
                 This is better than the route of [1,2,2,2,5], 
                 where the maximum absolute difference is 3.

    Example:
            [1,2,3]
            [3,8,4]
            [5,3,5]
    Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
    Output: 1
    Explanation: The route of [1,2,3,4,5] has a maximum 
                 absolute difference of 1 in consecutive 
                 cells, which is better than route 
                 [1,3,5,3,5].

    Example:
            [1,2,1,1,1]
            [1,2,1,2,1]
            [1,2,1,2,1]
            [1,2,1,2,1]
            [1,1,1,2,1]
    Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
    Output: 0
    Explanation: This route does not require any effort.

    Constraints:
        - rows == heights.length
        - columns == heights[i].length
        - 1 <= rows, columns <= 100
        - 1 <= heights[i][j] <= 10^6
'''
#Difficuty: Medium
#75 / 75 test cases passed.
#Runtime: 5840 ms
#Memory Usage: 28 MB

#Runtime: 5840 ms, faster than 5.03% of Python3 online submissions for Path With Minimum Effort.
#Memory Usage: 28 MB, less than 5.18% of Python3 online submissions for Path With Minimum Effort.

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        self.rows = len(heights) - 1
        self.cols = len(heights[0]) - 1
        lo = 0
        hi = max(max(heights, key=max))
        while lo < hi:
            mid = (lo+hi) // 2
            visited = self.dfs(heights, 0, 0, mid, set())
            if (self.rows, self.cols) in visited:
                hi = mid
            else:
                lo = mid+1
        return hi

    def dfs(self, heights, row, col, k, visited):
        visited.add((row, col))
        for x, y in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            if 0 <= row+x <= self.rows and 0 <= col+y <= self.cols and (row+x, col+y) not in visited and abs(heights[row][col] - heights[row+x][col+y]) <= k:
                self.dfs(heights, row+x, col+y, k, visited)
        return visited