"""
    Given a n-ary tree, find its maximum depth.
    The maximum depth is the number of nodes along the longest path from the 
    root node down to the farthest leaf node.
    Nary-Tree input serialization is represented in their level order traversal, 
    each group of children is separated by the null value (See examples).

    Example:
            1
          / | \
         3  2  4
        / \
       5   6

    Input: root = [1,null,3,2,4,null,5,6]
    Output: 3

    Constraints:
        - The depth of the n-ary tree is less than or equal to 1000.
        - The total number of nodes is between [0, 10^4].
"""
#Difficulty: Easy
#37 / 37 test cases passed.
#Runtime: 60 ms
#Memory Usage: 15.8 MB

#Runtime: 60 ms, faster than 30.66% of Python3 online submissions for Maximum Depth of N-ary Tree.
#Memory Usage: 15.8 MB, less than 16.99% of Python3 online submissions for Maximum Depth of N-ary Tree.

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        depth = 0
        queue = [root]
        while queue:
            length = len(queue)
            depth += 1
            while length:
                node = queue.pop(0)
                for child in node.children:
                    queue.append(child)
                length -= 1
        return depth
