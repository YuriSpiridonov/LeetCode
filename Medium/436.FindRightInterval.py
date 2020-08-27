"""
    Given a set of intervals, for each of the interval i, check if there exists 
    an interval j whose start point is bigger than or equal to the end point of 
    the interval i, which can be called that j is on the "right" of i.
    For any interval i, you need to store the minimum interval j's index, which 
    means that the interval j has the minimum start point to build the "right" 
    relationship for interval i. If the interval j doesn't exist, store -1 for 
    the interval i. Finally, you need output the stored value of each interval 
    as an array.

    Note:
        1. You may assume the interval's end point is always bigger than its 
           start point.
        2. You may assume none of these intervals have the same start point.

    Example:
    Input: [ [1,2] ]
    Output: [-1]
    Explanation: There is only one interval in the collection, so it outputs -1.

    Example:
    Input: [ [3,4], [2,3], [1,2] ]
    Output: [-1, 0, 1]
    Explanation: There is no satisfied "right" interval for [3,4].
                 For [2,3], the interval [3,4] has minimum-"right" start point;
                 For [1,2], the interval [2,3] has minimum-"right" start point.

    Example:
    Input: [ [1,4], [2,3], [3,4] ]
    Output: [-1, 2, -1]
    Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
                 For [2,3], the interval [3,4] has minimum-"right" start point.

    NOTE: input types have been changed on April 15, 2019. Please reset to 
          default code definition to get new method signature.
"""
#Difficulty: Medium
#17 / 17 test cases passed.
#Runtime: 8264 ms
#Memory Usage: 19.4 MB

#Runtime: 8264 ms, faster than 5.18% of Python3 online submissions for Find Right Interval.
#Memory Usage: 19.4 MB, less than 30.05% of Python3 online submissions for Find Right Interval.

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start = []
        end = []
        right_intervals = []
        for interval in intervals:
            start.append(interval[0])
            end.append(interval[1])
        for endpoint in end:
            if endpoint in start:
                right_intervals.append(start.index(endpoint))
            elif endpoint <= max(start):
                while endpoint <= max(start):
                    endpoint += 1
                    if endpoint in start:
                        right_intervals.append(start.index(endpoint))
                        break
            else:
                right_intervals.append(-1)
        return right_intervals
