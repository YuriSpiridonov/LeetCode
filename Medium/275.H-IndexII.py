"""
    Given an array of citations sorted in ascending order (each citation is a 
    non-negative integer) of a researcher, write a function to compute the 
    researcher's h-index.
    According to the definition of h-index on Wikipedia: "A scientist has index 
    h if h of his/her N papers have at least h citations each, and the other 
    N − h papers have no more than h citations each."
    
    Example:
    Input: citations = [0,1,3,5,6]
    Output: 3 
    Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and 
                 each of them had 
                 received 0, 1, 3, 5, 6 citations respectively. 
                 Since the researcher has 3 papers with at least 3 citations 
                 each and the remaining 
                 two with no more than 3 citations each, her h-index is 3.
    Note:
    If there are several possible values for h, the maximum one is taken as 
    the h-index.
    
    Follow up:
    - This is a follow up problem to H-Index, where citations is now guaranteed 
      to be sorted in ascending order.
    - Could you solve it in logarithmic time complexity?
"""
#Difficulty: Medium
#84 / 84 test cases passed.
#Runtime: 144 ms
#Memory Usage: 20.4 MB

#Runtime: 144 ms, faster than 89.79% of Python3 online submissions for H-Index II.
#Memory Usage: 20.4 MB, less than 50.00% of Python3 online submissions for H-Index II.

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        if len(citations) == 1:
            return min(len(citations), citations[0])
        citations = sorted(citations, reverse = True)
        for i, h in enumerate(citations):
            if h <= i:
                return i
        return len(citations)
