'''
    Given a string, your task is to count how many palindromic 
    substrings in this string.

    The substrings with different start indexes or end indexes 
    are counted as different substrings even they consist of 
    same characters.

    Example:
    Input: "abc"
    Output: 3
    Explanation: Three palindromic strings: "a", "b", "c".

    Example:
    Input: "aaa"
    Output: 6
    Explanation: Six palindromic strings: "a", "a", "a", 
                 "aa", "aa", "aaa".

    Note:
        1. The input string length won't exceed 1000.
'''
#Difficulty: Medium
#130 / 130 test cases passed.
#Runtime: 112 ms
#Memory Usage: 14.1 MB

#Runtime: 112 ms, faster than 93.62% of Python3 online submissions for Palindromic Substrings.
#Memory Usage: 14.1 MB, less than 88.49% of Python3 online submissions for Palindromic Substrings.

class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        length = len(s)
        for i in range(length):
            result += self.countPalindroms(s, i, i, length)
            result += self.countPalindroms(s, i, i+1, length)
        return result

    def countPalindroms(self, s: str, left: int, right: int, length: int) -> int:
        count = 0
        while left >= 0 and right < length:
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
            count += 1
        return count