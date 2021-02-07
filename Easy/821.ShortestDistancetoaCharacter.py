'''
    Given a string s and a character c that occurs in s, 
    return an array of integers answer where 
    answer.length == s.length and answer[i] is the shortest 
    distance from s[i] to the character c in s.

    Example:
    Input: s = "loveleetcode", c = "e"
    Output: [3,2,1,0,1,0,0,1,2,2,1,0]

    Example:
    Input: s = "aaab", c = "b"
    Output: [3,2,1,0]

    Constraints:
        - 1 <= s.length <= 10^4
        - s[i] and c are lowercase English letters.
        - c occurs at least once in s.
'''
#Difficuly: Easy
#76 / 76 test cases passed.
#Runtime: 92 ms
#Memory Usage: 14.4 MB

#Runtime: 92 ms, faster than 17.22% of Python3 online submissions for Shortest Distance to a Character.
#Memory Usage: 14.4 MB, less than 32.19% of Python3 online submissions for Shortest Distance to a Character.

class Solution:

    def shortestToChar(self, S: str, C: str) -> List[int]:
        left = self.pathBuilder(S, C)
        right = self.pathBuilder(S[::-1], C)[::-1]
        return [min(left[i], right[i]) for i in range(len(left))]

    def pathBuilder(self, S: str, C: str) -> List[int]:
        chars = list(S)
        chars[0] = S.index(C)
        for i in range(1, len(S)):
            if C in chars[i:]:
                if type(chars[i-1]) == int and chars[i-1] > 0:
                    chars[i] = chars[i-1] - 1
                elif (chars[i-1] == 0 or chars[i-1] == C):
                    chars[i] = chars[i:].index(C)
            elif chars[i] != 0:
                chars[i] = chars[i-1] + 1
        return chars