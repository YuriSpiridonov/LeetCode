"""
    Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing 
    moving one unit north, south, east, or west, respectively. You start at the 
    origin (0, 0) on a 2D plane and walk on the path specified by path.

    Return True if the path crosses itself at any point, that is, if at any time 
    you are on a location you've previously visited. Return False otherwise.

    Example:
    Input: path = "NESWW"
    Output: true
    Explanation: Notice that the path visits the origin twice.

    Constraints:
        - 1 <= path.length <= 10^4
        - path will only consist of characters in {'N', 'S', 'E', 'W}
"""
#Difficulty: Easy
#76 / 76 test cases passed.
#Runtime: 40 ms
#Memory Usage: 14 MB

#Runtime: 40 ms, faster than 36.06% of Python3 online submissions for Path Crossing.
#Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Path Crossing.

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        db = {"N" : [1, 0], "S" : [-1, 0], "E" : [0, 1], "W" : [0, -1]}
        moves = [[0, 0]]
        for i in path:
            moves.append([moves[-1][0] + db[i][0], moves[-1][1] + db[i][1]])
            if moves[-1] in moves[:-1]:
                return True
        return False
