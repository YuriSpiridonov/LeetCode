"""
    Given an n-ary tree, return the preorder traversal of its nodes' values.
    Nary-Tree input serialization is represented in their level order traversal, 
    each group of children is separated by the null value (See examples).

    Follow up:
    Recursive solution is trivial, could you do it iteratively?

    Example:
    Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]

    Constraints:
        - The height of the n-ary tree is less than or equal to 1000
        - The total number of nodes is between [0, 10^4]

"""
#Difficulty: Easy
#37 / 37 test cases passed.
#Runtime: 68 ms
#Memory Usage: 15.7 MB

#Runtime: 68 ms, faster than 26.94% of Python3 online submissions for N-ary Tree Preorder Traversal.
#Memory Usage: 15.7 MB, less than 62.80% of Python3 online submissions for N-ary Tree Preorder Traversal.

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        preorder = []
        self.traverse(root, preorder)
        return preorder

    def traverse(self, root, preorder):
        if not root:
            return
        preorder.append(root.val)
        for child in root.children:
            self.traverse(child, preorder)
