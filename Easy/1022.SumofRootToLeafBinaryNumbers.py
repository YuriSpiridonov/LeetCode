"""
    Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path 
    represents a binary number starting with the most significant bit.  
    For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could 
    represent 01101 in binary, which is 13.
    For all leaves in the tree, consider the numbers represented by the path 
    from the root to that leaf.
    Return the sum of these numbers.

    Example:
                 1
               /   \
              0     1
             / \   / \
            0   1 0   1

    Input: [1,0,1,0,1,0,1]
    Output: 22
    Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

    Note:
        1. The number of nodes in the tree is between 1 and 1000.
        2. node.val is 0 or 1.
        3. The answer will not exceed 2^31 - 1.
"""
#Difficulty: Easy
#63 / 63 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14 MB

#Runtime: 32 ms, faster than 93.41% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
#Memory Usage: 14 MB, less than 84.55% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.binary = []
        self.dfs(root)
        return sum(self.binary)

    def dfs(self, root, bi = ''):
        if not root:
            return
        bi += str(root.val)
        self.dfs(root.left, bi)
        self.dfs(root.right, bi)
        if not root.left and not root.right:
            self.binary.append(int(bi, 2))
