'''
    You are given a string word that consists of digits and 
    lowercase English letters.

    You will replace every non-digit character with a space. 
    For example, "a123bc34d8ef34" will become " 123  34 8  34". 
    Notice that you are left with some integers that are 
    separated by at least one space: "123", "34", "8", and 
    "34".

    Return the number of different integers after performing 
    the replacement operations on word.

    Two integers are considered different if their decimal 
    representations without any leading zeros are different.

    Example:
    Input: word = "a123bc34d8ef34"
    Output: 3
    Explanation: The three different integers are "123", 
                 "34", and "8". Notice that "34" is only 
                 counted once.

    Example:
    Input: word = "leet1234code234"
    Output: 2

    Example:
    Input: word = "a1b01c001"
    Output: 1
    Explanation: The three integers "1", "01", and "001" 
                 all represent the same integer because the 
                 leading zeros are ignored when comparing 
                 their decimal values.

    Constraints:
        - 1 <= word.length <= 1000
        - word consists of digits and lowercase English 
          letters.
'''
#Dfficulty: Easy
#85 / 85 test cases passed.
#Runtime: 24 ms
#Memory Usage: 14.2 MB

#Runtime: 24 ms, faster than 97.61% of Python3 online submissions for Number of Different Integers in a String.
#Memory Usage: 14.2 MB, less than 56.59% of Python3 online submissions for Number of Different Integers in a String.

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        number = ''
        numbers = set()
        word += 'a'
        for i in range(len(word)):
            if word[i].isdigit():
                number += word[i]
            else:
                if number:
                    numbers.add(int(number))
                    number = ''
        return len(numbers)
