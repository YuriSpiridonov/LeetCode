"""
    Given an n-ary tree, return the postorder traversal of its nodes' values.
    Nary-Tree input serialization is represented in their level order traversal, 
    each group of children is separated by the null value (See examples).

    Follow up:
    Recursive solution is trivial, could you do it iteratively?

    Example:
    Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]

    Constraints:
        - The height of the n-ary tree is less than or equal to 1000
        - The total number of nodes is between [0, 10^4]
"""
#Difficulty: Easy
#37 / 37 test cases passed.
#Runtime: 60 ms
#Memory Usage: 15.6 MB

#Runtime: 60 ms, faster than 35.99% of Python3 online submissions for N-ary Tree Postorder Traversal.
#Memory Usage: 15.6 MB, less than 87.13% of Python3 online submissions for N-ary Tree Postorder Traversal.

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        postorder = []
        self.traverse(root, postorder)
        return postorder

    def traverse(self, root, postorder):
        if not root:
            return
        for child in root.children:
            self.traverse(child, postorder)
        postorder.append(root.val)
