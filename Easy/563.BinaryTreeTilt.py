"""
    Given the root of a binary tree, return the sum of every tree node's tilt.

    The tilt of a tree node is the absolute difference between the sum of all 
    left subtree node values and all right subtree node values. If a node does 
    not have a left child, then the sum of the left subtree node values is 
    treated as 0. The rule is similar if there the node does not have 
    a right child.

    Example:
    Input: root = [1,2,3]
    Output: 1
    Explanation: 
                 Tilt of node 2 : |0-0| = 0 (no children)
                 Tilt of node 3 : |0-0| = 0 (no children)
                 Tile of node 1 : |2-3| = 1 (left subtree is just left child, 
                 so sum is 2; right subtree is just right child, so sum is 3)
                 Sum of every tilt : 0 + 0 + 1 = 1

    Example:
    Input: root = [4,2,9,3,5,null,7]
    Output: 15
    Explanation: 
                 Tilt of node 3 : |0-0| = 0 (no children)
                 Tilt of node 5 : |0-0| = 0 (no children)
                 Tilt of node 7 : |0-0| = 0 (no children)
                 Tilt of node 2 : |3-5| = 2 (left subtree is just left child, 
                 so sum is 3; right subtree is just right child, so sum is 5)
                 Tilt of node 9 : |0-7| = 7 (no left child, so sum is 0; right 
                 subtree is just right child, so sum is 7)
                 Tilt of node 4 : |(3+5+2)-(9+7)| = |10-16| = 6 (left subtree 
                 values are 3, 5, and 2, which sums to 10; right subtree 
                 values are 9 and 7, which sums to 16)
                 Sum of every tilt : 0 + 0 + 0 + 2 + 7 + 6 = 15

    Example:
    Input: root = [21,7,14,1,1,2,2,3,3]
    Output: 9

    Constraints:
        - The number of nodes in the tree is in the range [0, 10^4].
        - -1000 <= Node.val <= 1000
"""
#Difficulty: Easy
#77 / 77 test cases passed.
#Runtime: 576 ms
#Memory Usage: 15.8 MB

#Runtime: 576 ms, faster than 6.98% of Python3 online submissions for Binary Tree Tilt.
#Memory Usage: 15.8 MB, less than 96.11% of Python3 online submissions for Binary Tree Tilt.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def findTilt(self, root: TreeNode) -> int:
        self.result = 0
        self.postorder(root)
        return self.result

    def postorder(self, root):
        if not root:
            return 0
        self.postorder(root.left)
        self.postorder(root.right)
        self.result += abs(self.total(root.left) - self.total(root.right))

    def total(self, root):
        if not root:
            return 0
        return self.total(root.left) + self.total(root.right) + root.val
