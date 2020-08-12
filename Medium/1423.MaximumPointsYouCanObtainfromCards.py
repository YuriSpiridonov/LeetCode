"""
    There are several cards arranged in a row, and each card has an associated 
    number of points The points are given in the integer array cardPoints.
    In one step, you can take one card from the beginning or from the end of 
    the row. You have to take exactly k cards.
    Your score is the sum of the points of the cards you have taken.
    Given the integer array cardPoints and the integer k, return the maximum 
    score you can obtain.

    Example:
    Input: cardPoints = [1,2,3,4,5,6,1], k = 3
    Output: 12
    Explanation: After the first step, your score will always be 1. However, 
                 choosing the rightmost card first will maximize your total 
                 score. The optimal strategy is to take the three cards on the 
                 right, giving a final score of 1 + 6 + 5 = 12.

    Constraints:
        - 1 <= cardPoints.length <= 10^5
        - 1 <= cardPoints[i] <= 10^4
        - 1 <= k <= cardPoints.length
"""
#Difficulty: Medium
#40 / 40 test cases passed.
#Runtime: 464 ms
#Memory Usage: 26.8 MB

#Runtime: 464 ms, faster than 76.94% of Python3 online submissions for Maximum Points You Can Obtain from Cards.
#Memory Usage: 26.8 MB, less than 89.35% of Python3 online submissions for Maximum Points You Can Obtain from Cards.

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        i = 0
        l = len(cardPoints)
        total = sum(cardPoints)
        points = sum(cardPoints[:k])
        window = sum(cardPoints[i:l-k+i])
        while l - k + i < l:
            points = max(points, total - window)
            window = window - cardPoints[i] + cardPoints[l-k+i]
            i += 1
        return points
