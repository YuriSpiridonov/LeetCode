"""
    Given a non-empty special binary tree consisting of nodes with the 
    non-negative value, where each node in this tree has exactly two or zero 
    sub-node. If the node has two sub-nodes, then this node's value is the 
    smaller value among its two sub-nodes. More formally, the property 
    root.val = min(root.left.val, root.right.val) always holds.
    Given such a binary tree, you need to output the second minimum value in 
    the set made of all the nodes' value in the whole tree.
    If no such second minimum value exists, output -1 instead.

    Example:
    Input: 
            2
           / \
          2   5
             / \
            5   7

    Output: 5
    Explanation: The smallest value is 2, the second smallest value is 5.
"""
#Difficulty: Easy
#Status: Accepted
#Runtime: 28 ms
#Memory Usage: 13.6 MB

#Runtime: 28 ms, faster than 81.10% of Python3 online submissions for Second Minimum Node In a Binary Tree.
#Memory Usage: 13.6 MB, less than 94.96% of Python3 online submissions for Second Minimum Node In a Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        result = []
        self.preorder(root, result)
        return sorted(result)[1] if len(result) > 1 else -1

    def preorder(self, root, result):
        if not root:
            return 0
        if root.val not in result:
            result.append(root.val)
        if root.left:
            self.preorder(root.left, result)
        if root.right:
            self.preorder(root.right, result)
