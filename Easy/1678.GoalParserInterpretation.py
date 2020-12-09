'''
    You own a Goal Parser that can interpret a string command. 
    The command consists of an alphabet of "G", "()" and/or 
    "(al)" in some order. The Goal Parser will interpret "G" 
    as the string "G", "()" as the string "o", and "(al)" as 
    the string "al". The interpreted strings are then 
    concatenated in the original order.

    Given the string command, return the Goal Parser's 
    interpretation of command.

    Example:
    Input: command = "G()(al)"
    Output: "Goal"
    Explanation: The Goal Parser interprets the command as 
                 follows:
                 G -> G
                 () -> o
                 (al) -> al
                 The final concatenated result is "Goal".

    Example:
    Input: command = "G()()()()(al)"
    Output: "Gooooal"

    Example:
    Input: command = "(al)G(al)()()G"
    Output: "alGalooG"

    Constraints:
        - 1 <= command.length <= 100
        - command consists of "G", "()", and/or "(al)" in some 
          order.
'''
#Difficulty:Easy
#105 / 105 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14.1 MB

#Runtime: 32 ms, faster than 77.40% of Python3 online submissions for Goal Parser Interpretation.
#Memory Usage: 14.1 MB, less than 90.67% of Python3 online submissions for Goal Parser Interpretation.

class Solution:
    def interpret(self, command: str) -> str:
        command = list(command)
        l = False
        for i, char in enumerate(command):
            if char == 'l':
                l = True
            elif char == '(':
                command[i] = ''
            elif char == ')':
                command[i] = '' if l else 'o'
                l = False
        return ''.join(command)
