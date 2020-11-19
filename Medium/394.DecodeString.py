"""
    Given an encoded string, return its decoded string.

    The encoding rule is: k[encoded_string], where the encoded_string inside 
    the square brackets is being repeated exactly k times. Note that k is 
    guaranteed to be a positive integer.

    You may assume that the input string is always valid; No extra white 
    spaces, square brackets are well-formed, etc.

    Furthermore, you may assume that the original data does not contain any 
    digits and that digits are only for those repeat numbers, k. For example, 
    there won't be input like 3a or 2[4].

    Example:
    Input: s = "3[a]2[bc]"
    Output: "aaabcbc"

    Example:
    Input: s = "3[a2[c]]"
    Output: "accaccacc"

    Example:
    Input: s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"

    Example:
    Input: s = "abc3[cd]xyz"
    Output: "abccdcdcdxyz"

    Constraints:
        - 1 <= s.length <= 30
        - s consists of lowercase English letters, digits, and square 
          brackets '[]'.
        - s is guaranteed to be a valid input.
        - All the integers in s are in the range [1, 300].
"""
#Difficulty: Medium
#31 / 31 test cases passed.
#Runtime: 28 ms
#Memory Usage: 14.1 MB

#Runtime: 28 ms, faster than 70.66% of Python3 online submissions for Decode String.
#Memory Usage: 14.1 MB, less than 70.09% of Python3 online submissions for Decode String.

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ']':
                string = ''
                x = ''
                while stack and stack[-1].isalpha():
                    string = stack.pop() + string
                stack.pop()
                while stack and stack[-1].isdigit():
                    x = stack.pop() + x
                stack.append(string*int(x))
            else:
                stack.append(char)
        return ''.join(stack)
