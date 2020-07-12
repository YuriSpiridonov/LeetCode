"""
    Given an n-ary tree, return the level order traversal of its nodes' values.
    Nary-Tree input serialization is represented in their level order traversal, 
    each group of children is separated by the null value (See examples).

    Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

    Constraints:
        - The height of the n-ary tree is less than or equal to 1000
        - The total number of nodes is between [0, 10^4]
"""
#Difficulty: Medium
#37 / 37 test cases passed.
#Runtime: 48 ms
#Memory Usage: 15.6 MB

#Runtime: 48 ms, faster than 94.40% of Python3 online submissions for N-ary Tree Level Order Traversal.
#Memory Usage: 15.6 MB, less than 67.55% of Python3 online submissions for N-ary Tree Level Order Traversal. 

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return None
        depth = 0
        queue = {depth : [root]}
        while queue:
            if depth > len(queue)-1:
                break
            level = queue[depth]
            for i in range(len(level)):
                if level[i].children:
                    if depth+1 in queue:
                        queue[depth+1] += level[i].children
                    else:
                        queue[depth+1] = level[i].children
                level[i] = level[i].val
            depth += 1
        return queue.values()
