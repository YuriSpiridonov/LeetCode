"""
    Given a string s. You should re-order the string using the following 
    algorithm:
        1. Pick the smallest character from s and append it to the result.
        2. Pick the smallest character from s which is greater than the last 
           appended character to the result and append it.
        3. Repeat step 2 until you cannot pick more characters.
        4. Pick the largest character from s and append it to the result.
        5. Pick the largest character from s which is smaller than the last 
           appended character to the result and append it.
        6. Repeat step 5 until you cannot pick more characters.
        7. Repeat the steps from 1 to 6 until you pick all characters from s.

    In each step, If the smallest or the largest character appears more than 
    once you can choose any occurrence and append it to the result.

    Return the result string after sorting s with this algorithm.

    Example:
    Input: s = "aaaabbbbcccc"
    Output: "abccbaabccba"
    Explanation: After steps 1, 2 and 3 of the first iteration, 
                 result = "abc"
                 After steps 4, 5 and 6 of the first iteration, 
                 result = "abccba"
                 First iteration is done. Now s = "aabbcc" and we go back to 
                 step 1
                 After steps 1, 2 and 3 of the second iteration, 
                 result = "abccbaabc"
                 After steps 4, 5 and 6 of the second iteration, 
                 result = "abccbaabccba"

    Example:
    Input: s = "rat"
    Output: "art"
    Explanation: The word "rat" becomes "art" after re-ordering it with the 
                 mentioned algorithm.

    Example:
    Input: s = "leetcode"
    Output: "cdelotee"

    Example:
    Input: s = "ggggggg"
    Output: "ggggggg"

    Example:
    Input: s = "spo"
    Output: "ops"

    Constraints:
        - 1 <= s.length <= 500
        - s contains only lower-case English letters.
"""
#Difficulty: Easy
#323 / 323 test cases passed.
#Runtime: 52 ms
#Memory Usage: 14 MB

#Runtime: 52 ms, faster than 96.96% of Python3 online submissions for Increasing Decreasing String.
#Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Increasing Decreasing String.

class Solution:
    def sortString(self, s: str) -> str:
        result = ''
        letters = [0] * 26
        chars = set(s)
        for char in chars:
            letters[ord(char) - 97] = s.count(char)
        while True:
            for i in range(26):
                if letters[i]:
                    result += chr(i + 97)
                    letters[i] -= 1
            for l in range(25, -1, -1):
                if letters[l]:
                    result += chr(l + 97)
                    letters[l] -= 1
            if sum(letters) == 0:
                break
        return result
