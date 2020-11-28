"""
    Given a string text, you want to use the characters of text to form as 
    many instances of the word "balloon" as possible.

    You can use each character in text at most once. Return the maximum 
    number of instances that can be formed.

    Example:
    Input: text = "nlaebolko"
    Output: 1

    Example:
    Input: text = "loonbalxballpoon"
    Output: 2

    Example:
    Input: text = "leetcode"
    Output: 0

    Constraints:
        - 1 <= text.length <= 10^4
        - text consists of lower case English letters only.
"""
#Difficulty: Easy
#23 / 23 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14.3 MB

#Runtime: 32 ms, faster than 67.90% of Python3 online submissions for Maximum Number of Balloons.
#Memory Usage: 14.3 MB, less than 53.34% of Python3 online submissions for Maximum Number of Balloons.

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloons = float(inf)
        for char in 'balon':
            if char in 'lo':
                balloons = min(balloons, text.count(char) // 2)
            else:
                balloons = min(balloons, text.count(char))
        return balloons
