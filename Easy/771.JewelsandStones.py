"""
    You're given strings J representing the types of stones that are jewels, 
    and S representing the stones you have.  Each character in S is a type of 
    stone you have.  You want to know how many of the stones you have are also 
    jewels.
    
    The letters in J are guaranteed distinct, and all characters in J and S 
    are letters. Letters are case sensitive, so "a" is considered a different 
    type of stone from "A".
    
    Example:
    Input: J = "aA", S = "aAAbbbb"
    Output: 3
"""
#Difficulty: Easy
#254 / 254 test cases passed.
#Runtime: 40 ms
#Memory Usage: 14 MB

#Runtime: 40 ms, faster than 23.33% of Python3 online submissions for Jewels and Stones.
#Memory Usage: 14 MB, less than 5.39% of Python3 online submissions for Jewels and Stones.

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        i = len(J) - 1
        count = 0
        while i >= 0:
            if J[i] in S:
                count += S.count(J[i])
            i -= 1
        return count

#Runtime: 32 ms, faster than 29.66% of Python3 online submissions for Jewels and Stones.
#Memory Usage: 13.7 MB, less than 5.39% of Python3 online submissions for Jewels and Stones.
    
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for letter in J:
            count += S.count(letter)
        return count
    
#Runtime: 24 ms, faster than 92.03% of Python3 online submissions for Jewels and Stones.
#Memory Usage: 13.5 MB, less than 5.39% of Python3 online submissions for Jewels and Stones.
        
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum([S.count(letter) for letter in list(J)])
