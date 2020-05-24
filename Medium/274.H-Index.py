"""
    Given an array of citations (each citation is a non-negative integer) of a 
    researcher, write a function to compute the researcher's h-index.
    According to the definition of h-index on Wikipedia: "A scientist has 
    index h if h of his/her N papers have at least h citations each, and the 
    other N − h papers have no more than h citations each."
    
    Example:
    Input: citations = [3,0,6,1,5]
    Output: 3 
    Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and 
                 each of them had received 3, 0, 6, 1, 5 citations respectively. 
                 Since the researcher has 3 papers with at least 3 citations 
                 each and the remaining two with no more than 3 citations each, 
                 her h-index is 3.
    Note: If there are several possible values for h, the maximum one is taken 
    as the h-index.
"""
#Difficulty: Medium
#82 / 82 test cases passed.
#Runtime: 28 ms
#Memory Usage: 14 MB

#Runtime: 28 ms, faster than 97.30% of Python3 online submissions for H-Index.
#Memory Usage: 14 MB, less than 14.29% of Python3 online submissions for H-Index.

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
