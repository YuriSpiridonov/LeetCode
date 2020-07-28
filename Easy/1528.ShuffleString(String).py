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
#Runtime: 72 ms
#Memory Usage: 13.8 MB

#Runtime: 72 ms, faster than 69.20% of Python3 online submissions for Shuffle String.
#Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Shuffle String.

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l = len(s)
        shuffle = "_" * l
        for i in range(l):
            shuffle = shuffle[:indices[i]] + s[i] + shuffle[indices[i]+1:]
        return shuffle
