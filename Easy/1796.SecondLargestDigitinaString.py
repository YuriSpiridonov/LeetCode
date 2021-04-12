'''
    Given an alphanumeric string s, return the second 
    largest numerical digit that appears in s, or -1 if it 
    does not exist.

    An alphanumeric string is a string consisting of 
    lowercase English letters and digits.

    Example:
    Input: s = "dfa12321afd"
    Output: 2
    Explanation: The digits that appear in s are [1, 2, 3]. 
                 The second largest digit is 2.

    Example:
    Input: s = "abc1111"
    Output: -1
    Explanation: The digits that appear in s are [1]. There 
                 is no second largest digit. 

    Constraints:
        - 1 <= s.length <= 500
        - s consists of only lowercase English letters 
          and/or digits.
'''
#Difficulty: Easy
#301 / 301 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14.1 MB

#Runtime: 32 ms, faster than 92.59% of Python3 online submissions for Second Largest Digit in a String.
#Memory Usage: 14.1 MB, less than 94.39% of Python3 online submissions for Second Largest Digit in a String.

class Solution:
    def secondHighest(self, s: str) -> int:
        n = set()
        n.add(-1)
        for c in s:
            if 48 <= ord(c) <= 57:
                n.add(int(c))
        n = sorted(n)
        if n[-1] >= 0:
            n.pop()
        return n[-1]