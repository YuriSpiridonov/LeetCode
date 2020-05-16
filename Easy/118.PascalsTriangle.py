"""
    Given a non-negative integer numRows, generate the first numRows of 
    Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly 
    above it.
    
    Example:
    Input: 5
    Output:
    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    ]
"""
#Difficulty: Easy
#15 / 15 test cases passed.
#Runtime: 28 ms
#Memory Usage: 13.6 MB

#Runtime: 28 ms, faster than 72.51% of Python3 online submissions for Pascal's Triangle.
#Memory Usage: 13.6 MB, less than 7.14% of Python3 online submissions for Pascal's Triangle.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows: return None
        triangle = [[1]]
        for n in range(1, numRows):
            t = triangle[n-1]
            l = [t[0], t[-1]]
            while len(l) < n+1:
                for i in range(1, len(t)):
                    l.insert(len(l) - 1, t[i-1] + t[i])
            triangle.extend([l])
        return triangle
