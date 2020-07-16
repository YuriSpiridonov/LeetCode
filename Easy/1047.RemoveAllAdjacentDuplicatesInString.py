"""
    Given a string S of lowercase letters, a duplicate removal consists of 
    choosing two adjacent and equal letters, and removing them.
    We repeatedly make duplicate removals on S until we no longer can.
    Return the final string after all such duplicate removals have been made.
    It is guaranteed the answer is unique.

    Example:
    Input: "abbaca"
    Output: "ca"
    Explanation: 
    For example, in "abbaca" we could remove "bb" since the letters are 
    adjacent and equal, and this is the only possible move.  The result of this 
    move is that the string is "aaca", of which only "aa" is possible, so the 
    final string is "ca".

    Note:
        1. 1 <= S.length <= 20000
        2. S consists only of English lowercase letters.
"""
#Difficulty: Easy
#98 / 98 test cases passed.
#Runtime: 128 ms
#Memory Usage: 13.7 MB

#Runtime: 128 ms, faster than 25.09% of Python3 online submissions for Remove All Adjacent Duplicates In String.
#Memory Usage: 13.7 MB, less than 98.64% of Python3 online submissions for Remove All Adjacent Duplicates In String.

class Solution:
    def removeDuplicates(self, S: str) -> str:
        i = 0
        while True:
            if i + 1 > len(S) - 1:
                break
            if S[i] == S[i+1]:
                S = S[:i] + S[i+2:]
                i = max(i-1, 0)
            else:
                i += 1
        return S
