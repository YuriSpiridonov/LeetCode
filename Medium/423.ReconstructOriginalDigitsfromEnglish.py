'''
    Given a non-empty string containing an out-of-order 
    English representation of digits 0-9, output the digits 
    in ascending order.

    Note:
        1. Input contains only lowercase English letters.
        2. Input is guaranteed to be valid and can be t
           ransformed to its original digits. That means 
           invalid inputs such as "abc" or "zerone" are not 
           permitted.
        3. Input length is less than 50,000.

    Example:
    Input: "owoztneoer"
    Output: "012"

    Example:
    Input: "fviefuro"
    Output: "45"
'''
#Difficulty: Medium
#24 / 24 test cases passed.
#Runtime: 44 ms
#Memory Usage: 14.5 MB

#Runtime: 44 ms, faster than 87.21% of Python3 online submissions for Reconstruct Original Digits from English.
#Memory Usage: 14.5 MB, less than 66.28% of Python3 online submissions for Reconstruct Original Digits from English.

from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        letters_count = {'z': ['0', {'z': 1, 'e': 1, 'r': 1, 'o': 1}], 
                         'o': ['1', {'o': 1, 'n': 1, 'e': 1}], 
                         'w': ['2', {'t': 1, 'w': 1, 'o': 1}], 
                         't': ['3', {'t': 1, 'h': 1, 'r': 1, 'e': 2}], 
                         'u': ['4', {'f': 1, 'o': 1, 'u': 1, 'r': 1}], 
                         'f': ['5', {'f': 1, 'i': 1, 'v': 1, 'e': 2}], 
                         'x': ['6', {'s': 1, 'i': 1, 'x': 1}], 
                         's': ['7', {'s': 1, 'e': 2, 'v': 1, 'n': 1}], 
                         'g': ['8', {'e': 1, 'i': 1, 'g': 1, 'h': 1, 't': 1}], 
                         'i': ['9', {'n': 2, 'i': 1, 'e': 1}]}
        uniques = ['z', 'o', 'w', 't', 'u', 'f', 'x', 's', 'g', 'i']
        order = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
        s = Counter(s)
        result = []

        for i in order:
            count = s[uniques[i]]
            result.append(letters_count[uniques[i]][0] * count)
            for char in letters_count[uniques[i]][1]:
                s[char] -= letters_count[uniques[i]][1][char] * count
        return ''.join(sorted(result))
