"""
    There is a robot starting at position (0, 0), the origin, on a 2D plane. 
    Given a sequence of its moves, judge if this robot ends up at (0, 0) after 
    it completes its moves.

    The move sequence is represented by a string, and the character moves[i] 
    represents its ith move. Valid moves are R (right), L (left), U (up), and 
    D (down). If the robot returns to the origin after it finishes all of its 
    moves, return true. Otherwise, return false.

    Note: The way that the robot is "facing" is irrelevant. "R" will always 
    make the robot move to the right once, "L" will always make it move left, 
    etc. Also, assume that the magnitude of the robot's movement is the same 
    for each move.

    Example:
    Input: "UD"
    Output: true 
    Explanation: The robot moves up once, and then down once. All moves have 
                 the same magnitude, so it ended up at the origin where it 
                 started. Therefore, we return true.

    Example:
    Input: "LL"
    Output: false
    Explanation: The robot moves left twice. It ends up two "moves" to the left 
                 of the origin. We return false because it is not at the origin 
                 at the end of its moves.
"""
#Difficulty: Easy
#63 / 63 test cases passed.
#Runtime: 48 ms
#Memory Usage: 13.7 MB

#Runtime: 48 ms, faster than 84.21% of Python3 online submissions for Robot Return to Origin.
#Memory Usage: 13.7 MB, less than 93.39% of Python3 online submissions for Robot Return to Origin.

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        path = {'L' : 0, 'R' : 0, 'U' : 0, 'D' : 0}
        for move in moves:
            path[move] += 1
        return path['L'] == path['R'] and path['U'] == path['D']
