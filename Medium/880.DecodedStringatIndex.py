'''
    An encoded string S is given. To find and write the decoded 
    string to a tape, the encoded string is read one character 
    at a time and the following steps are taken:
        - If the character read is a letter, that letter is 
          written onto the tape.
        - If the character read is a digit (say d), the entire 
          current tape is repeatedly written d-1 more times in 
          total.

    Now for some encoded string S, and an index K, find and 
    return the K-th letter (1 indexed) in the decoded string.

    Example:
    Input: S = "leet2code3", K = 10
    Output: "o"
    Explanation: The decoded string is 
                 "leetleetcodeleetleetcodeleetleetcode".
                 The 10th letter in the string is "o".

    Example:
    Input: S = "ha22", K = 5
    Output: "h"
    Explanation: he decoded string is "hahahaha".  
                 The 5th letter is "h".

    Example:
    Input: S = "a2345678999999999999999", K = 1
    Output: "a"
    Explanation: The decoded string is "a" repeated 
                 8301530446056247680 times.  The 1st letter 
                 is "a".

    Constraints:
        - 2 <= S.length <= 100
        - S will only contain lowercase letters and digits 2 
          through 9.
        - S starts with a letter.
        - 1 <= K <= 10^9
        - It's guaranteed that K is less than or equal to the 
          length of the decoded string.
        - The decoded string is guaranteed to have less than 
          2^63 letters.
'''
#Difficulty: Medium
#45 / 45 test cases passed.
#Runtime: 28 ms
#Memory Usage: 14.3 MB

#Runtime: 28 ms, faster than 75.81% of Python3 online submissions for Decoded String at Index.
#Memory Usage: 14.3 MB, less than 19.76% of Python3 online submissions for Decoded String at Index.

class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        i = 0
        length = 0
        while i <= len(S) - 1 and length <= K:
            if S[i].isdigit():
                length *= int(S[i])
            else:
                length += 1
            i += 1
        i -= 1
        while i >= 0 and (length > K or S[i].isdigit()):
            if S[i].isdigit():
                length //= int(S[i])
                K = K % length if K % length else length
            else:
                length -= 1
            i -= 1
        return S[max(0, i)]
