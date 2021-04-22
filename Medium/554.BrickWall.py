'''
    There is a brick wall in front of you. The wall is 
    rectangular and has several rows of bricks. The bricks 
    have the same height but different width. You want to 
    draw a vertical line from the top to the bottom and 
    cross the least bricks.

    The brick wall is represented by a list of rows. Each 
    row is a list of integers representing the width of each 
    brick in this row from left to right.

    If your line go through the edge of a brick, then the 
    brick is not considered as crossed. You need to find 
    out how to draw the line to cross the least bricks and 
    return the number of crossed bricks.

    You cannot draw a line just along one of the two vertical 
    edges of the wall, in which case the line will obviously 
    cross no bricks.

    Example:
    Input: [[1,2,2,1],
            [3,1,2],
            [1,3,2],
            [2,4],
            [3,1,2],
            [1,3,1,1]]

    Output: 2

    Note:
        1. The width sum of bricks in different rows are 
           the same and won't exceed INT_MAX.
        2. The number of bricks in each row is in range 
           [1,10,000]. The height of wall is in range 
           [1,10,000]. Total number of bricks of the wall 
           won't exceed 20,000.
'''
#Difficulty: Medium
#85 / 85 test cases passed.
#Runtime: 176 ms
#Memory Usage: 18.9 MB

#Runtime: 176 ms, faster than 84.56% of Python3 online submissions for Brick Wall.
#Memory Usage: 18.9 MB, less than 99.11% of Python3 online submissions for Brick Wall.

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        length = len(wall)
        table = {}
        for bricks in wall:
            array = []
            for val in bricks[:-1]:
                if not array:
                    array.append(val)
                else:
                    array.append(array[-1]+val)
            for val in array:
                if val not in table:
                    table[val] = 0
                table[val] += 1
        return length - max(table.values()) if table else length