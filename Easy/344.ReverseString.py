"""
    Write a function that reverses a string. The input string is given as an 
    array of characters char[].
    Do not allocate extra space for another array, you must do this by 
    modifying the input array in-place with O(1) extra memory.
    You may assume all the characters consist of printable ascii characters.
    
    Example:
    Input: ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]
"""
#Difficulty: Easy
#478 / 478 test cases passed.
#Runtime: 204 ms
#Memory Usage: 18 MB

#Runtime: 204 ms, faster than 91.57% of Python3 online submissions for Reverse String.
#Memory Usage: 18 MB, less than 5.81% of Python3 online submissions for Reverse String.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        l = len(s) - 1
        while i <= l:
            s[i], s[l] = s[l], s[i]
            i += 1
            l -= 1
        return s
