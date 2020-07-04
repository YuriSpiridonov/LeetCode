"""
    Given the root node of a binary search tree, return the sum of values of 
    all nodes with value between L and R (inclusive).
    The binary search tree is guaranteed to have unique values.

    Example:
    Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
    Output: 32

    Note:
        1. The number of nodes in the tree is at most 10000.
        2. The final answer is guaranteed to be less than 2^31.
"""
#Difficulty: Easy
#42 / 42 test cases passed.
#Runtime: 240 ms
#Memory Usage: 22 MB

#Runtime: 240 ms, faster than 62.37% of Python3 online submissions for Range Sum of BST.
#Memory Usage: 22 MB, less than 38.97% of Python3 online submissions for Range Sum of BST.

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        summ = 0
        if not root:
            return 0
        if L <= root.val <= R:
            summ += root.val
        if root.val > L:
            summ += self.rangeSumBST(root.left, L, R)
        if root.val < R:
            summ += self.rangeSumBST(root.right, L, R)
        return summ
