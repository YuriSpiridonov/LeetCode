'''
    You are given a list of songs where the ith song has a duration of 
    time[i] seconds.

    Return the number of pairs of songs for which their total duration 
    in seconds is divisible by 60. Formally, we want the number of 
    indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

    Example:
    Input: time = [30,20,150,100,40]
    Output: 3
    Explanation: Three pairs have a total duration divisible by 60:
                 (time[0] = 30, time[2] = 150): total duration 180
                 (time[1] = 20, time[3] = 100): total duration 120
                 (time[1] = 20, time[4] = 40): total duration 60

    Example:
    Input: time = [60,60,60]
    Output: 3
    Explanation: All three pairs have a total duration of 120, which 
                 is divisible by 60.

    Constraints:
        - 1 <= time.length <= 6 * 104
        - 1 <= time[i] <= 500
'''
#Difficulty: Medium
#34 / 34 test cases passed.
#Runtime: 244 ms
#Memory Usage: 18.1 MB

#Runtime: 244 ms, faster than 20.48% of Python3 online submissions for Pairs of Songs With Total Durations Divisible by 60.
#Memory Usage: 18.1 MB, less than 9.49% of Python3 online submissions for Pairs of Songs With Total Durations Divisible by 60.


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        duration = {}
        for t in time:
            if t % 60 == 0 and 0 in duration:
                count += duration[0]
            elif 60 - t%60 in duration:
                count += duration[60 - t%60]
            if t % 60 not in duration:
                duration[t%60] = 0
            duration[t%60] += 1
        return count
