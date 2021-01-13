'''
    The i-th person has weight people[i], and each boat can 
    carry a maximum weight of limit.

    Each boat carries at most 2 people at the same time, 
    provided the sum of the weight of those people is at 
    most limit.

    Return the minimum number of boats to carry every given 
    person. (It is guaranteed each person can be carried by 
    a boat.)

    Example:
    Input: people = [1,2], limit = 3
    Output: 1
    Explanation: 1 boat (1, 2)

    Example:
    Input: people = [3,2,2,1], limit = 3
    Output: 3
    Explanation: 3 boats (1, 2), (2) and (3)

    Example:
    Input: people = [3,5,3,4], limit = 5
    Output: 4
    Explanation: 4 boats (3), (3), (4), (5)

    Note:
        - 1 <= people.length <= 50000
        - 1 <= people[i] <= limit <= 30000
'''
#Difficulty: Medium
#77 / 77 test cases passed.
#Runtime: 444 ms
#Memory Usage: 21 MB

#Runtime: 444 ms, faster than 81.09% of Python3 online submissions for Boats to Save People.
#Memory Usage: 21 MB, less than 49.42% of Python3 online submissions for Boats to Save People.

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        i = 0
        j = len(people) - 1
        people.sort()
        while i <= j:
            if people[i] <= limit - people[j]:
                i += 1
            boats += 1
            j -= 1
        return boats
