'''
    Given a string containing digits from 2-9 inclusive, 
    return all possible letter combinations that the number 
    could represent. Return the answer in any order.

    A mapping of digit to letters (just like on the 
    telephone buttons) is given below. Note that 1 does not 
    map to any letters.

    Example:
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

    Example:
    Input: digits = ""
    Output: []

    Example:
    Input: digits = "2"
    Output: ["a","b","c"]

    Constraints:
        - 0 <= digits.length <= 4
        - digits[i] is a digit in the range ['2', '9'].
'''
#Difficulty: Medium
#25 / 25 test cases passed.
#Runtime: 28 ms
#Memory Usage: 14.2 MB

#Runtime: 28 ms, faster than 81.79% of Python3 online submissions for Letter Combinations of a Phone Number.
#Memory Usage: 14.2 MB, less than 86.13% of Python3 online submissions for Letter Combinations of a Phone Number.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        length = len(digits)
        letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        return self.dfs(digits, letters, length, [], '', 0)
    
    def dfs(self, digits, letters, length, result, combination, current):
        if current == length:
            result.append(combination)
            return
        for char in letters[digits[current]]:
            self.dfs(digits, letters, length, result, combination+char, current+1)
        return result
