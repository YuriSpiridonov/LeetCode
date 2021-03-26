'''
    We are given two arrays A and B of words.  Each word is 
    a string of lowercase letters.

    Now, say that word b is a subset of word a if every 
    letter in b occurs in a, including multiplicity.  For 
    example, "wrr" is a subset of "warrior", but is not a 
    subset of "world".

    Now say a word a from A is universal if for every b in 
    B, b is a subset of a. 

    Return a list of all universal words in A. You can 
    return the words in any order.

    Example:
    Input: A = ["amazon","apple","facebook","google","leetcode"], 
           B = ["e","o"]
    Output: ["facebook","google","leetcode"]

    Example:
    Input: A = ["amazon","apple","facebook","google","leetcode"], 
           B = ["l","e"]
    Output: ["apple","google","leetcode"]

    Example:
    Input: A = ["amazon","apple","facebook","google","leetcode"], 
           B = ["e","oo"]
    Output: ["facebook","google"]

    Example:
    Input: A = ["amazon","apple","facebook","google","leetcode"], 
           B = ["lo","eo"]
    Output: ["google","leetcode"]

    Example:
    Input: A = ["amazon","apple","facebook","google","leetcode"], 
           B = ["ec","oc","ceo"]
    Output: ["facebook","leetcode"]

    Note:
        1. 1 <= A.length, B.length <= 10000
        2. 1 <= A[i].length, B[i].length <= 10
        3. A[i] and B[i] consist only of lowercase letters.
        4. All words in A[i] are unique: there isn't i != j 
           with A[i] == A[j].
'''
#Difficulty: Medium
#55 / 55 test cases passed.
#Runtime: 776 ms
#Memory Usage: 17.8 MB

#Runtime: 776 ms, faster than 77.37% of Python3 online submissions for Word Subsets.
#Memory Usage: 17.8 MB, less than 99.16% of Python3 online submissions for Word Subsets.

from collections import Counter

class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        result = []
        unique = {}
        # Counting unique characters 
        for b in B:
            chars = Counter(b)
            for char in chars:
                if char not in unique:
                    unique[char] = chars[char]
                else:
                    unique[char] = max(unique[char], chars[char])
        # Comparing with unique characters
        for a in A:
            word = Counter(a)
            subset = True
            for char in unique:
                if char not in word or word[char] < unique[char]:
                    subset = False
                    break
            if subset:
                result.append(a)
        return result