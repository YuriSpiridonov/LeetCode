"""
    Given a binary tree, check whether it is a mirror of itself 
    (ie, symmetric around its center).

    For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
            1
           / \
          2   2
         / \ / \
        3  4 4  3

    But the following [1,2,2,null,3,null,3] is not:
            1
           / \
          2   2
           \   \
           3    3

    Follow up: Solve it both recursively and iteratively.
"""
#Difficulty: Easy
#195 / 195 test cases passed.
#Runtime: 28 ms
#Memory Usage: 14.1 MB

#Runtime: 28 ms, faster than 95.44% of Python3 online submissions for Symmetric Tree.
#Memory Usage: 14.1 MB, less than 23.72% of Python3 online submissions for Symmetric Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root]
        while queue:
            length = len(queue)
            level = []
            while length:
                node = queue.pop(0)
                level.append(node.val if node else None)
                length -= 1
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
            i = 0
            j = len(level) - 1
            while i <= j:
                if level[i] != level[j]:
                    return False
                i += 1
                j -= 1
        return True
