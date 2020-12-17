'''
    You have n  tiles, where each tile has one letter tiles[i] 
    printed on it.

    Return the number of possible non-empty sequences of 
    letters you can make using the letters printed on those 
    tiles.

    Example:
    Input: tiles = "AAB"
    Output: 8
    Explanation: The possible sequences are "A", "B", "AA", 
                 "AB", "BA", "AAB", "ABA", "BAA".

    Example:
    Input: tiles = "AAABBC"
    Output: 188

    Example:
    Input: tiles = "V"
    Output: 1

    Constraints:
        - 1 <= tiles.length <= 7
        - tiles consists of uppercase English letters.
'''
#Difficulty: Medium
#86 / 86 test cases passed.
#Runtime: 80 ms
#Memory Usage: 15.3 MB

#Runtime: 80 ms, faster than 63.69% of Python3 online submissions for Letter Tile Possibilities.
#Memory Usage: 15.3 MB, less than 57.87% of Python3 online submissions for Letter Tile Possibilities.

from itertools import permutations

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = 0
        for i in range(1, len(tiles)+1):
            n += len(set(permutations(tiles, i)))
        return n
