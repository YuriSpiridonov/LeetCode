'''
    In an election, the i-th vote was cast for persons[i] 
    at time times[i].

    Now, we would like to implement the following query 
    function: TopVotedCandidate.q(int t) will return the 
    number of the person that was leading the election at 
    time t.  

    Votes cast at time t will count towards our query.
    In the case of a tie, the most recent vote (among tied 
    candidates) wins.

    Example:
    Input: ["TopVotedCandidate","q","q","q","q","q","q"], 
           [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
    Output: [null,0,1,1,0,0,1]
    Explanation: 
                 - At time 3, the votes are [0], and 0 is 
                   leading.
                 - At time 12, the votes are [0,1,1], and 
                   1 is leading.
                 - At time 25, the votes are [0,1,1,0,0,1], 
                   and 1 is leading (as ties go to the most 
                   recent vote.)
                 - This continues for 3 more queries at 
                   time 15, 24, and 8.

    Note:
        1. 1 <= persons.length = times.length <= 5000
        2. 0 <= persons[i] <= persons.length
        3. times is a strictly increasing array with all 
           elements in [0, 10^9].
        4. TopVotedCandidate.q is called at most 10000 times 
           per test case.
        5. TopVotedCandidate.q(int t) is always called with 
           t >= times[0].
'''
#Difficulty: Medium
#97 / 97 test cases passed.
#Runtime: 944 ms
#Memory Usage: 19.5 MB

#Runtime: 944 ms, faster than 25.39% of Python3 online submissions for Online Election.
#Memory Usage: 19.5 MB, less than 45.39% of Python3 online submissions for Online Election.

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = self.votes(persons)
        self.times = times

    def q(self, t: int) -> int:
        left = 0
        right = len(self.times) - 1
        while left <= right:
            middle = (left+right) // 2
            if self.times[middle] == t:
                return self.persons[middle]
            elif self.times[middle] > t:
                right = middle - 1
            else:
                left = middle + 1
        return self.persons[left-1]

    def votes(self, persons: List[int]) -> List[int]:
        votes = {}
        current_leader = persons[0]
        leader_board = []
        for person in persons:
            if person not in votes:
                votes[person] = 0
            votes[person] += 1
            if votes[person] >= votes[current_leader]:
                current_leader = person
            leader_board.append(current_leader)
        return leader_board


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
