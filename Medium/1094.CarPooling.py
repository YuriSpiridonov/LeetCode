"""
    You are driving a vehicle that has capacity empty seats initially available 
    for passengers.  The vehicle only drives east (ie. it cannot turn around 
    and drive west.)
    Given a list of trips, 
    trip[i] = [num_passengers, start_location, end_location] contains 
    information about the i-th trip: the number of passengers that must be 
    picked up, and the locations to pick them up and drop them off.  
    The locations are given as the number of kilometers due east from your 
    vehicle's initial location.
    Return true if and only if it is possible to pick up and drop off all 
    passengers for all the given trips. 

    Example:
    Input: trips = [[2,1,5],[3,3,7]], capacity = 4
    Output: false

    Example:
    Input: trips = [[2,1,5],[3,3,7]], capacity = 5
    Output: true

    Example:
    Input: trips = [[2,1,5],[3,5,7]], capacity = 3
    Output: true

    Example:
    Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
    Output: true

    Constraints:
        1. trips.length <= 1000
        2. trips[i].length == 3
        3. 1 <= trips[i][0] <= 100
        4. 0 <= trips[i][1] < trips[i][2] <= 1000
        5. 1 <= capacity <= 100000
"""
#Difficulty: Medium
#54 / 54 test cases passed.
#Runtime: 64 ms
#Memory Usage: 14.2 MB

#Runtime: 64 ms, faster than 76.30% of Python3 online submissions for Car Pooling.
#Memory Usage: 14.2 MB, less than 68.86% of Python3 online submissions for Car Pooling.

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        destinations = [0] * 1000
        for trip in trips:
            destinations[trip[1]] += trip[0]
            destinations[trip[2]] -= trip[0]
        for i in range(1, len(destinations)):
            destinations[i] += destinations[i-1]
            if destinations[i] > capacity:
                return False
        return True
