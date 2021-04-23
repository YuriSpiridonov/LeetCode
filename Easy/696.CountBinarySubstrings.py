'''
    Give a string s, count the number of non-empty (contiguous) 
    substrings that have the same number of 0's and 1's, 
    and all the 0's and all the 1's in these substrings are 
    grouped consecutively.

    Substrings that occur multiple times are counted the 
    number of times they occur.

    Example:
    Input: "00110011"
    Output: 6
    Explanation: There are 6 substrings that have equal number 
                 of consecutive 1's and 0's: "0011", "01", 
                 "1100", "10", "0011", and "01".

                Notice that some of these substrings repeat 
                and are counted the number of times they occur.

                Also, "00110011" is not a valid substring 
                because all the 0's (and 1's) are not grouped 
                together.

    Example:
    Input: "10101"
    Output: 4
    Explanation: There are 4 substrings: "10", "01", "10", 
                 "01" that have equal number of consecutive 
                 1's and 0's.

    Note:
        - s.length will be between 1 and 50,000.
        - s will only consist of "0" or "1" characters.
'''
#Difficulty: Easy
#90 / 90 test cases passed.
#Runtime: 300 ms
#Memory Usage: 14.5 MB

#Runtime: 300 ms, faster than 7.82% of Python3 online submissions for Count Binary Substrings.
#Memory Usage: 14.5 MB, less than 74.34% of Python3 online submissions for Count Binary Substrings.

class Solution:

    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                count += self.count(s, i, i+1, s[i], s[i+1])
        return count

    def count(self, s: str, i: int, j: int, l: str, r: str) -> int:
        while i >= 0 and j < len(s) and s[i] == l and s[j] == r:
            i -= 1
            j += 1
        return (j-i)//2