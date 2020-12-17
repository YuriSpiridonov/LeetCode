'''
    Given the array queries of positive integers between 1 
    and m, you have to process all queries[i] (from i=0 to 
    i=queries.length-1) according to the following rules:
        - In the beginning, you have the permutation 
          P=[1,2,3,...,m].
        - For the current i, find the position of queries[i] 
          in the permutation P (indexing from 0) and then move 
          this at the beginning of the permutation P. Notice 
          that the position of queries[i] in P is the result 
          for queries[i].

    Return an array containing the result for the given queries.

    Example:
    Input: queries = [3,1,2,1], m = 5
    Output: [2,1,2,1] 
    Explanation: The queries are processed as follow: 
                 - For i=0: queries[i]=3, P=[1,2,3,4,5], 
                   position of 3 in P is 2, then we move 3 
                   to the beginning of P resulting in 
                   P=[3,1,2,4,5]. 
                 - For i=1: queries[i]=1, P=[3,1,2,4,5], 
                   position of 1 in P is 1, then we move 1 
                   to the beginning of P resulting in 
                   P=[1,3,2,4,5]. 
                 - For i=2: queries[i]=2, P=[1,3,2,4,5], 
                   position of 2 in P is 2, then we move 2 
                   to the beginning of P resulting in 
                   P=[2,1,3,4,5]. 
                 - For i=3: queries[i]=1, P=[2,1,3,4,5], 
                   position of 1 in P is 1, then we move 1 
                   to the beginning of P resulting in 
                   P=[1,2,3,4,5]. 
                 - Therefore, the array containing the result 
                   is [2,1,2,1].  

    Example:
    Input: queries = [4,1,2,2], m = 4
    Output: [3,1,2,0]

    Example:
    Input: queries = [7,5,5,8,3], m = 8
    Output: [6,5,0,7,5]

    Constraints:
        - 1 <= m <= 10^3
        - 1 <= queries.length <= m
        - 1 <= queries[i] <= m
'''
#Difficulty: Medium
#53 / 53 test cases passed.
#Runtime: 48 ms
#Memory Usage: 14.6 MB

#Runtime: 48 ms, faster than 97.70% of Python3 online submissions for Queries on a Permutation With Key.
#Memory Usage: 14.6 MB, less than 11.49% of Python3 online submissions for Queries on a Permutation With Key.

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        permutation = [n for n in range(1, m+1)]
        for i, n in enumerate(queries):
            queries[i] = permutation.index(n)
            permutation.insert(0, permutation.pop(queries[i]))
        return queries
