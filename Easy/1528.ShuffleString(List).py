"""
    Given a string s and an integer array indices of the same length.
    The string s will be shuffled such that the character at the ith position 
    moves to indices[i] in the shuffled string.
    Return the shuffled string.

    Example:
    Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
    Output: "leetcode"
    Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

    Constraints:
        - s.length == indices.length == n
        - 1 <= n <= 100
        - s contains only lower-case English letters.
        - 0 <= indices[i] < n
        - All values of indices are unique (i.e. indices is a permutation of 
          the integers from 0 to n - 1).
"""
#Difficulty: Easy
#399 / 399 test cases passed.
#Runtime: 52 ms
#Memory Usage: 13.8 MB

#Runtime: 52 ms, faster than 97.33% of Python3 online submissions for Shuffle String.
#Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Shuffle String.

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l = len(s)
        shuffle = [None] * l
        for i in range(l):
            shuffle[indices[i]] = s[i]
        return ''.join(shuffle)
