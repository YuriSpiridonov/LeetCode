"""
    Given a string, sort it in decreasing order based on the frequency of 
    characters.
    
    Example:
    Input:
        "Aabb"
    Output:
        "bbAa"
    Explanation:
        "bbaA" is also a valid answer, but "Aabb" is incorrect.
        Note that 'A' and 'a' are treated as two different characters.
"""
#Difficulty: Medium
#35 / 35 test cases passed.
#Runtime: 20 ms
#Memory Usage: 14.9 MB

#Runtime: 20 ms, faster than 100.00% of Python3 online submissions for Sort Characters By Frequency.
#Memory Usage: 14.9 MB, less than 14.29% of Python3 online submissions for Sort Characters By Frequency.

class Solution:
    def frequencySort(self, s: str) -> str:
        letters = set(s)
        d = {}
        result = ''
        for letter in letters:
            count =  s.count(letter)
            if count not in d:
                d[count] = [letter * count]
            else:
                d[count].append(letter * count)
        keys = sorted(d.keys(), reverse=True)
        for key in keys:
            for letter in d[key]:
                result += letter
        return result
