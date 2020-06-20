"""
    Create a timebased key-value store class TimeMap, that supports two operations.

    1. set(string key, string value, int timestamp)
        - Stores the key and value, along with the given timestamp.

    2. get(string key, int timestamp)
        - Returns a value such that set(key, value, timestamp_prev) was called 
          previously, with timestamp_prev <= timestamp.
        - If there are multiple such values, it returns the one with the largest 
          timestamp_prev.
        - If there are no values, it returns the empty string ("").

    Example:
    Input: inputs = ["TimeMap","set","get","get","set","get","get"], 
           inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
    Output: [null,null,"bar","bar",null,"bar2","bar2"]

    Explanation:
    TimeMap kv;
    kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with 
                             // timestamp = 1   
    kv.get("foo", 1);        // output "bar"   
    kv.get("foo", 3);        // output "bar" since there is no value corresponding 
                             // to foo at timestamp 3 and timestamp 2, then the 
                             // only value is at timestamp 1 ie "bar"   
    kv.set("foo", "bar2", 4);   
    kv.get("foo", 4);        // output "bar2"   
    kv.get("foo", 5);        // output "bar2"   

    Note:
        1. All key/value strings are lowercase.
        2. All key/value strings have length in the range [1, 100]
        3. The timestamps for all TimeMap.set operations are strictly increasing.
        4. 1 <= timestamp <= 10^7
        5. TimeMap.set and TimeMap.get functions will be called a total of 
           120000 times (combined) per test case.
"""
#Difficulty: Medium
#45 / 45 test cases passed.
#Runtime: 936 ms
#Memory Usage: 73.4 MB

#Runtime: 936 ms, faster than 23.22% of Python3 online submissions for Time Based Key-Value Store.
#Memory Usage: 73.4 MB, less than 5.20% of Python3 online submissions for Time Based Key-Value Store.

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.KeyDB = {}
        self.ValueDB = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.KeyDB:
            self.KeyDB[key].append(timestamp)
        else:
            self.KeyDB[key] = [timestamp]
        if timestamp in self.ValueDB:
            self.ValueDB[timestamp].append(value)
        else:
            self.ValueDB[timestamp] = [value]

    def get(self, key: str, timestamp: int) -> str:
        lo = 0
        hi = len(self.KeyDB[key]) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.KeyDB[key][mid] == timestamp:
                return self.ValueDB[timestamp][-1]
            elif self.KeyDB[key][mid] < timestamp:
                lo = mid + 1
            else:
                hi = mid - 1
        return "" if self.KeyDB[key][hi] >= timestamp else self.ValueDB[self.KeyDB[key][hi]][-1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
