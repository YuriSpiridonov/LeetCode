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
#Runtime: 316 ms
#Memory Usage: 21.7 MB

#Runtime: 316 ms, faster than 20.89% of Python3 online submissions for Range Sum of BST.
#Memory Usage: 21.7 MB, less than 94.93% of Python3 online submissions for Range Sum of BST.

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        summ = 0
        if not root:
            return 0
        if L <= root.val <= R:
            summ += root.val
        summ += self.rangeSumBST(root.left, L, R)
        summ += self.rangeSumBST(root.right, L, R)
        return summ
