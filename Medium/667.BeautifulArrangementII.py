'''
    Given two integers n and k, you need to construct a list 
    which contains n different positive integers ranging 
    from 1 to n and obeys the following requirement:
    Suppose this list is [a1, a2, a3, ... , an], then the 
    list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] 
    has exactly k distinct integers.

    If there are multiple answers, print any of them.

    Example:
    Input: n = 3, k = 1
    Output: [1, 2, 3]
    Explanation: The [1, 2, 3] has three different positive 
                 integers ranging from 1 to 3, and the [1, 1] 
                 has exactly 1 distinct integer: 1.

    Example:
    Input: n = 3, k = 2
    Output: [1, 3, 2]
    Explanation: The [1, 3, 2] has three different positive 
                 integers ranging from 1 to 3, and the [2, 1] 
                 has exactly 2 distinct integers: 1 and 2.

    Note:
        1. The n and k are in the range 1 <= k < n <= 10^4.
'''
#Difficuty: Medium
#68 / 68 test cases passed.
#Runtime: 52 ms
#Memory Usage: 15.7 MB

#Runtime: 52 ms, faster than 26.00% of Python3 online submissions for Beautiful Arrangement II.
#Memory Usage: 15.7 MB, less than 6.67% of Python3 online submissions for Beautiful Arrangement II.

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        array = []
        visited = set()
        k += 1
        for i in range(n):
            i += 1
            if i not in visited:
                array.append(i)
                visited.add(i)
            if k not in visited:
                array.append(k)
                visited.add(k)
                k -= 1
        return array