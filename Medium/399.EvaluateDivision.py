"""
    You are given equations in the format A / B = k, where A and B are variables 
    represented as strings, and k is a real number (floating-point number). 
    Given some queries, return the answers. If the answer does not exist, 
    return -1.0.
    The input is always valid. You may assume that evaluating the queries will 
    result in no division by zero and there is no contradiction.

    Example:
    Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], 
           queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
    Explanation: 
                Given: a / b = 2.0, b / c = 3.0
                queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
                return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

    Example:
    Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], 
           queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    Output: [3.75000,0.40000,5.00000,0.20000]

    Example:
    Input: equations = [["a","b"]], values = [0.5], 
           queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
    Output: [0.50000,2.00000,-1.00000,-1.00000]

    Constraints:
        - 1 <= equations.length <= 20
        - equations[i].length == 2
        - 1 <= equations[i][0], equations[i][1] <= 5
        - values.length == equations.length
        - 0.0 < values[i] <= 20.0
        - 1 <= queries.length <= 20
        - queries[i].length == 2
        - 1 <= queries[i][0], queries[i][1] <= 5
        - equations[i][0], equations[i][1], queries[i][0], queries[i][1] 
          consist of lower case English letters and digits.
"""
#Difficulty: Medium
#22 / 22 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14.2 MB

#Runtime: 32 ms, faster than 57.37% of Python3 online submissions for Evaluate Division.
#Memory Usage: 14.2 MB, less than 5.41% of Python3 online submissions for Evaluate Division.

from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        result = []
        numbers = defaultdict(list)
        for index, equation in enumerate(equations):
            numbers[equation[0]] += [(equation[1], values[index])]
            numbers[equation[1]] += [(equation[0], 1 / values[index])]
        for querie in queries:
            if querie[0] == querie[1] and querie[0] in numbers:
                result.append(1)
                continue
            queue = []
            visited = set()
            visited.add(querie[0])
            number = -1
            queue.append((querie[0], 1))
            while queue:
                key, value = queue.pop(0)
                if key == querie[1] and key in numbers:
                    number = value
                    break
                for k, v in numbers[key]:
                    if k in visited:
                        continue
                    queue.append((k, value * v))
                    visited.add(k)
            result.append(number)
        return result
