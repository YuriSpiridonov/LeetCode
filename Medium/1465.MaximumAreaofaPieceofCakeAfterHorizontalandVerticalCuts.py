'''
    Given a rectangular cake with height h and width w, and 
    two arrays of integers horizontalCuts and verticalCuts 
    where horizontalCuts[i] is the distance from the top of 
    the rectangular cake to the ith horizontal cut and 
    similarly, verticalCuts[j] is the distance from the left 
    of the rectangular cake to the jth vertical cut.

    Return the maximum area of a piece of cake after you cut 
    at each horizontal and vertical position provided in the 
    arrays horizontalCuts and verticalCuts. Since the answer 
    can be a huge number, return this modulo 10^9 + 7.

    Example:
    Input: h = 5, w = 4, horizontalCuts = [1,2,4], 
           verticalCuts = [1,3]
    Output: 4 
    Explanation: The figure above represents the given 
                 rectangular cake. Red lines are the 
                 horizontal and vertical cuts. After you cut 
                 the cake, the green piece of cake has the 
                 maximum area.

    Example:
    Input: h = 5, w = 4, horizontalCuts = [3,1], 
           verticalCuts = [1]
    Output: 6
    Explanation: The figure above represents the given 
                 rectangular cake. Red lines are the 
                 horizontal and vertical cuts. After you 
                 cut the cake, the green and yellow pieces 
                 of cake have the maximum area.

    Example:
    Input: h = 5, w = 4, horizontalCuts = [3], 
           verticalCuts = [3]
    Output: 9

    Constraints:
        - 2 <= h, w <= 10^9
        - 1 <= horizontalCuts.length < min(h, 10^5)
        - 1 <= verticalCuts.length < min(w, 10^5)
        - 1 <= horizontalCuts[i] < h
        - 1 <= verticalCuts[i] < w
        - It is guaranteed that all elements in h
          orizontalCuts are distinct.
        - It is guaranteed that all elements in 
          verticalCuts are distinct.
'''
#Difficulty: Medium
#53 / 53 test cases passed.
#Runtime: 352 ms
#Memory Usage: 32.6 MB

#Runtime: 352 ms, faster than 9.02% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
#Memory Usage: 32.6 MB, less than 5.19% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = [0] + sorted(horizontalCuts) + [h]
        verticalCuts = [0] + sorted(verticalCuts) + [w]

        horizontalDiff = []
        verticalDiff = []

        for i in range(1, len(horizontalCuts)):
            horizontalDiff.append(horizontalCuts[i] - horizontalCuts[i-1])
        for i in range(1, len(verticalCuts)):
            verticalDiff.append(verticalCuts[i] - verticalCuts[i-1])

        return max(horizontalDiff) * max(verticalDiff) % (10**9 + 7)
