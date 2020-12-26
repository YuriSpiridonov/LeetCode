'''
    Alice and Bob take turns playing a game, with Alice 
    starting first.

    Initially, there is a number N on the chalkboard.  
    On each player's turn, that player makes a move consisting 
    of:
        - Choosing any x with 0 < x < N and N % x == 0.
        - Replacing the number N on the chalkboard with N - x.

    Also, if a player cannot make a move, they lose the game.

    Return True if and only if Alice wins the game, assuming 
    both players play optimally.

    Example:
    Input: 2
    Output: true
    Explanation: Alice chooses 1, and Bob has no more moves.

    Example:
    Input: 3
    Output: false
    Explanation: Alice chooses 1, Bob chooses 1, and Alice 
                 has no more moves.

    Note:
        1. 1 <= N <= 1000
'''
#Difficulty: Easy
#40 / 40 test cases passed.
#Runtime: 28 ms
#Memory Usage: 14.2 MB

#Runtime: 28 ms, faster than 79.57% of Python3 online submissions for Divisor Game.
#Memory Usage: 14.2 MB, less than 51.41% of Python3 online submissions for Divisor Game.

class Solution:
    def divisorGame(self, N: int) -> bool:
        return not N % 2
