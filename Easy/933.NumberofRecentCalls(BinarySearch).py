"""
    Write a class RecentCounter to count recent requests.
    It has only one method: ping(int t), where t represents some time in
    milliseconds.
    Return the number of pings that have been made from 3000 milliseconds ago 
    until now.
    Any ping with time in [t - 3000, t] will count, including the current ping.
    It is guaranteed that every call to ping uses a strictly larger value of t 
    than before.

    Example:
    Input: inputs = ["RecentCounter","ping","ping","ping","ping"], 
           inputs = [[],[1],[100],[3001],[3002]]
    Output: [null,1,2,3,3]

    Note:
        1. Each test case will have at most 10000 calls to ping.
        2. Each test case will call ping with strictly increasing values of t.
        3. Each call to ping will have 1 <= t <= 10^9.
"""
#Difficulty: Easy
#68 / 68 test cases passed.
#Runtime: 604 ms
#Memory Usage: 18.3 MB

#Runtime: 604 ms, faster than 12.26% of Python3 online submissions for Number of Recent Calls.
#Memory Usage: 18.3 MB, less than 93.52% of Python3 online submissions for Number of Recent Calls.

class RecentCounter:

    def __init__(self):
        self.queue = []
 
    def ping(self, t: int) -> int:
        self.queue.append(t)
        self.queue[:] = self.queue[self.binarySearch(self.queue):]
        return len(self.queue)
     
    def binarySearch(self, queue):
        last_ping = queue[-1]
        l = 0
        r = len(queue)
        while l < r:
            m = (l + r) // 2
            if queue[m] == last_ping - 3000:
                return m
            elif queue[m] < last_ping - 3000:
                l = m + 1
            else:
                r = m
        return r
