"""
    Given two strings A and B of lowercase letters, return true if you can 
    swap two letters in A so the result is equal to B, otherwise, return false.

    Swapping letters is defined as taking two indices i and j (0-indexed) 
    such that i != j and swapping the characters at A[i] and A[j]. For example, 
    swapping at indices 0 and 2 in "abcd" results in "cbad".

    Example:
    Input: A = "ab", B = "ba"
    Output: true
    Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is 
                 equal to B.

    Example:
    Input: A = "ab", B = "ab"
    Output: false
    Explanation: The only letters you can swap are A[0] = 'a' and A[1] = 'b', 
                 which results in "ba" != B.

    Example:
    Input: A = "aa", B = "aa"
    Output: true
    Explanation: You can swap A[0] = 'a' and A[1] = 'a' to get "aa", which is 
                 equal to B.

    Example:
    Input: A = "aaaaaaabc", B = "aaaaaaacb"
    Output: true

    Example:
    Input: A = "", B = "aa"
    Output: false

    Constraints:
        - 0 <= A.length <= 20000
        - 0 <= B.length <= 20000
        - A and B consist of lowercase letters.
"""
#Difficulty: Easy
#29 / 29 test cases passed.
#Runtime: 196 ms
#Memory Usage: 14.4 MB

#Runtime: 196 ms, faster than 7.87% of Python3 online submissions for Buddy Strings.
#Memory Usage: 14.4 MB, less than 25.71% of Python3 online submissions for Buddy Strings.

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if not A or not B or len(A) != len(B):
            return False
        i = len(A) - 1
        index = None
        while i >= 0:
            if A[i] != B[i]:
                if not index:
                    index = i
                else:
                    B = list(B)
                    B[i], B[index] = B[index], B[i]
                    B = ''.join(B)
                    return A == B
            i -= 1
        if A == B:
            count = 0
            for char in A:
                count = max(count, A.count(char))
            return count > 1
        else:
            False
