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
#Runtime: 316 ms
#Memory Usage: 18.3 MB

#Runtime: 316 ms, faster than 46.58% of Python3 online submissions for Number of Recent Calls.
#Memory Usage: 18.3 MB, less than 96.93% of Python3 online submissions for Number of Recent Calls.
        
class RecentCounter:

    def __init__(self):
        self.queue = []
 
    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.pop(0)
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
