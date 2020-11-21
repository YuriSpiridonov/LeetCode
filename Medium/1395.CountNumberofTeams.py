"""
    There are n soldiers standing in a line. Each soldier is assigned a 
    unique rating value.

    You have to form a team of 3 soldiers amongst them under the following 
    rules:
        - Choose 3 soldiers with index (i, j, k) with rating 
          (rating[i], rating[j], rating[k]).
        - A team is valid if:  (rating[i] < rating[j] < rating[k]) or 
          (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).

    Return the number of teams you can form given the conditions. 
    (soldiers can be part of multiple teams).

    Example:
    Input: rating = [2,5,3,4,1]
    Output: 3
    Explanation: We can form three teams given the conditions. 
                 (2,3,4), (5,4,1), (5,3,1). 

    Example:
    Input: rating = [2,1,3]
    Output: 0
    Explanation: We can't form any team given the conditions.

    Example:
    Input: rating = [1,2,3,4]
    Output: 4

    Constraints:
        - n == rating.length
        - 1 <= n <= 200
        - 1 <= rating[i] <= 10^5
"""
#Difficulty: Medium
#53 / 53 test cases passed.
#Runtime: 1000 ms
#Memory Usage: 14.4 MB

#Runtime: 1000 ms, faster than 47.95% of Python3 online submissions for Count Number of Teams.
#Memory Usage: 14.4 MB, less than 12.89% of Python3 online submissions for Count Number of Teams.

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        length = len(rating)
        for i in range(length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    if rating[i] > rating[j] > rating[k]:
                        count += 1
                    elif rating[i] < rating[j] < rating[k]:
                        count += 1
        return count
