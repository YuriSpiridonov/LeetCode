"""
    Given a string s of lower and upper case English letters.
    A good string is a string which doesn't have two adjacent characters s[i] 
    and s[i + 1] where:
        - 0 <= i <= s.length - 2
        - s[i] is a lower-case letter and s[i + 1] is the same letter but in 
          upper-case or vice-versa.
    To make the string good, you can choose two adjacent characters that make 
    the string bad and remove them. You can keep doing this until the string 
    becomes good.
    Return the string after making it good. The answer is guaranteed to be 
    unique under the given constraints.
    Notice that an empty string is also good.

    Example:
    Input: s = "leEeetcode"
    Output: "leetcode"
    Explanation: In the first step, either you choose i = 1 or i = 2, both will 
                 result "leEeetcode" to be reduced to "leetcode".

    Example:
    Input: s = "abBAcC"
    Output: ""
    Explanation: We have many possible scenarios, and all lead to the same 
                 answer. For example:
                 "abBAcC" --> "aAcC" --> "cC" --> ""
                 "abBAcC" --> "abBA" --> "aA" --> ""

    Example:
    Input: s = "s"
    Output: "s"

    Constraints:
        - 1 <= s.length <= 100
        - s contains only lower and upper case English letters.
"""
#Difficulty: Easy
#334 / 334 test cases passed.
#Runtime: 36 ms
#Memory Usage: 13.8 MB

#Runtime: 36 ms, faster than 77.96% of Python3 online submissions for Make The String Great.
#Memory Usage: 13.8 MB, less than 76.77% of Python3 online submissions for Make The String Great.

class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while True:
            if i + 1 >= len(s):
                break
            elif ((s[i].isupper() and s[i+1].islower()) or (s[i].islower() and s[i+1].isupper())) and s[i].lower() == s[i+1].lower():
                s = s[:i] + s[i+2:]
                i = max(0, i - 1)
            else:
                i += 1
        return s
