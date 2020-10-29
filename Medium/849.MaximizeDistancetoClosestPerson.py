"""
    You are given an array representing a row of seats where seats[i] = 1 
    represents a person sitting in the ith seat, and seats[i] = 0 represents 
    that the ith seat is empty (0-indexed).

    There is at least one empty seat, and at least one person sitting.

    Alex wants to sit in the seat such that the distance between him and the 
    closest person to him is maximized. 

    Return that maximum distance to the closest person.

    Example:
               2      2
            <---->V<---->
            1  0  0  0  1  0  1 <- seats
            0  1  2  3  4  5  6 <- indices

    Input: seats = [1,0,0,0,1,0,1]
    Output: 2
    Explanation: 
                 If Alex sits in the second open seat (i.e. seats[2]), then 
                 the closest person has distance 2.
                 If Alex sits in any other open seat, the closest person has 
                 distance 1.
                 Thus, the maximum distance to the closest person is 2.

    Example:
    Input: seats = [1,0,0,0]
    Output: 3
    Explanation: 
                 If Alex sits in the last seat (i.e. seats[3]), the closest 
                 person is 3 seats away.
                 This is the maximum distance possible, so the answer is 3.

    Example:
    Input: seats = [0,1]
    Output: 1

    Constraints:
        - 2 <= seats.length <= 2 * 10**4
        - seats[i] is 0 or 1.
        - At least one seat is empty.
        - At least one seat is occupied.
"""
#Difficulty: Medium
#79 / 79 test cases passed.
#Runtime: 132 ms
#Memory Usage: 14.5 MB

#Runtime: 132 ms, faster than 72.64% of Python3 online submissions for Maximize Distance to Closest Person.
#Memory Usage: 14.5 MB, less than 42.01% of Python3 online submissions for Maximize Distance to Closest Person.

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        distance = 0
        max_distance = 0
        divisor = 1
        length = len(seats) - 1
        for i, seat in enumerate(seats):
            if (i == 0 or 0 < i < length and max_distance) and seat == 1:
                divisor = 2
            elif i == length and seat == 0:
                divisor = 1
            if seat == 0:
                distance += 1
            if i != 0 and seat == 1 and distance or i == length:
                if divisor == 2:
                    max_distance = max(max_distance, (distance + 1) // divisor)
                else:
                    max_distance = max(max_distance, distance)
                distance = 0
        return max_distance
