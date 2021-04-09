'''
    You are given coordinates, a string that represents the 
    coordinates of a square of the chessboard. Below is a 
    chessboard for your reference.

    Return true if the square is white, and false if the 
    square is black.

    The coordinate will always represent a valid chessboard 
    square. The coordinate will always have the letter first, 
    and the number second.

    Example:
    Input: coordinates = "a1"
    Output: false
    Explanation: From the chessboard above, the square with 
                 coordinates "a1" is black, so return false.

    Example:
    Input: coordinates = "h3"
    Output: true
    Explanation: From the chessboard above, the square with 
                 coordinates "h3" is white, so return true.

    Example:
    Input: coordinates = "c7"
    Output: false

    Constraints:
        - coordinates.length == 2
        - 'a' <= coordinates[0] <= 'h'
        - '1' <= coordinates[1] <= '8'
'''
#Dfficulty: Easy
#203 / 203 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14.1 MB

#Runtime: 32 ms, faster than 68.51% of Python3 online submissions for Determine Color of a Chessboard Square.
#Memory Usage: 14.1 MB, less than 71.83% of Python3 online submissions for Determine Color of a Chessboard Square.

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return not ord(coordinates[0]) % 2 == int(coordinates[1]) % 2