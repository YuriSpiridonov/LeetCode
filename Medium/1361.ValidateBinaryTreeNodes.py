'''
    You have n binary tree nodes numbered from 0 to n - 1 
    where node i has two children leftChild[i] and 
    rightChild[i], return true if and only if all the given 
    nodes form exactly one valid binary tree.

    If node i has no left child then leftChild[i] will equal 
    -1, similarly for the right child.

    Note that the nodes have no values and that we only use 
    the node numbers in this problem.

    Example:
            0
           / \
          1   2
             /
            3
    Input: n = 4, 
           leftChild = [1,-1,3,-1], 
           rightChild = [2,-1,-1,-1]
    Output: true

    Example:
            0
           / \
          1   2
           \ /
            3
    Input: n = 4, 
           leftChild = [1,-1,3,-1], 
           rightChild = [2,3,-1,-1]
    Output: false

    Example:
            0
           /
          1
    Input: n = 2, 
           leftChild = [1,0], 
           rightChild = [-1,-1]
    Output: false

    Example:
            0         3
           / \       / \
          1   2     3   5
    Input: n = 6, 
           leftChild = [1,-1,-1,4,-1,-1], 
           rightChild = [2,-1,-1,5,-1,-1]
    Output: false

    Constraints:
        - 1 <= n <= 10^4
        - leftChild.length == rightChild.length == n
        - -1 <= leftChild[i], rightChild[i] <= n - 1
'''
#Difficulty: Medium
#38 / 38 test cases passed.
#Runtime: 336 ms
#Memory Usage: 16.8 MB

#Runtime: 336 ms, faster than 43.66% of Python3 online submissions for Validate Binary Tree Nodes.
#Memory Usage: 16.8 MB, less than 63.94% of Python3 online submissions for Validate Binary Tree Nodes.

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        queue = []
        length = 0
        visited = set()
        nodes = set(leftChild + rightChild)
        for x in range(n):
            if x not in nodes:
                queue.append(x)
                break
        else:
            queue.append(0)
        while queue:
            i = queue.pop(0)
            if i != -1 and i not in visited:
                length += 1
                visited.add(i)
                queue.append(leftChild[i])
                queue.append(rightChild[i])
            elif i == -1:
                continue
            else:
                return False
        return length == n
