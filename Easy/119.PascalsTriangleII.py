"""
    Given a non-negative index k where k ≤ 33, return the kth index row of the 
    Pascal's triangle.
    Note that the row index starts from 0.
    
    In Pascal's triangle, each number is the sum of the two numbers directly 
    above it.
    
    Example:
    Input: 3
    Output: [1,3,3,1]
    Follow up:
    
    Could you optimize your algorithm to use only O(k) extra space?
"""
#Difficulty: Easy
#34 / 34 test cases passed.
#Runtime: 24 ms
#Memory Usage: 13.8 MB

#Runtime: 24 ms, faster than 92.36% of Python3 online submissions for Pascal's Triangle II.
#Memory Usage: 13.8 MB, less than 7.69% of Python3 online submissions for Pascal's Triangle II.

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1]]
        for n in range(1, rowIndex+1):
            t = triangle[n-1]
            l = [t[0], t[-1]]
            while len(l) < n+1:
                for i in range(1, len(t)):
                    l.insert(len(l) - 1, t[i-1] + t[i])
            triangle.extend([l])
        return triangle[-1]
