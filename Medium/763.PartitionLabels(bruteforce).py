"""
    A string S of lowercase English letters is given. We want to partition this 
    string into as many parts as possible so that each letter appears in at 
    most one part, and return a list of integers representing the size of these 
    parts.

    Example:
    Input: S = "ababcbacadefegdehijhklij"
    Output: [9,7,8]
    Explanation: The partition is "ababcbaca", "defegde", "hijhklij".
                 This is a partition so that each letter appears in at most one 
                 part.
                 A partition like "ababcbacadefegde", "hijhklij" is incorrect, 
                 because it splits S into less parts.

    Note:
        - S will have length in range [1, 500].
        - S will consist of lowercase English letters ('a' to 'z') only.
"""
#Difficulty: Medium
#116 / 116 test cases passed.
#Runtime: 116 ms
#Memory Usage: 13.9 MB

#Runtime: 116 ms, faster than 5.27% of Python3 online submissions for Partition Labels.
#Memory Usage: 13.9 MB, less than 45.67% of Python3 online submissions for Partition Labels.

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        result = []
        last_index = {}
        length = len(S)
        letters = set(S)
        for char in letters:
            i = S.index(char)
            l = length - 1
            while l >= i:
                if S[l] == char:
                    last_index[S[l]] = [i, l]
                    break
                l -= 1
        ranges = sorted(list(last_index.values()))
        result.append(ranges.pop(0))
        while ranges:
            rnge = ranges.pop(0)
            for i in range(len(result)):
                if set(range(result[i][0], result[i][1]+1)).intersection(set(range(rnge[0], rnge[1]+1))):
                    result[i][0] = min(result[i][0], rnge[0])
                    result[i][1] = max(result[i][1], rnge[1])
                    break
            if not set(range(result[i][0], result[i][1]+1)).intersection(set(range(rnge[0], rnge[1]+1))):
                result.extend([rnge])
        for i in range(len(result)):
            result[i] = 1 + result[i][1] - result[i][0]
        return result
