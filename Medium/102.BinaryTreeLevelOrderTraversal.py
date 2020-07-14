"""
    Given a binary tree, return the level order traversal of its nodes' values. 
    (ie, from left to right, level by level).

    For example:
    Given binary tree [3,9,20,null,null,15,7],
            3
           / \
          9  20
            /  \
           15   7
    return its level order traversal as:
        [
          [3],
          [9,20],
          [15,7]
        ]
"""
#Difficulty: Medium
#34 / 34 test cases passed.
#Runtime: 28 ms
#Memory Usage: 14.1 MB

#Runtime: 28 ms, faster than 95.46% of Python3 online submissions for Binary Tree Level Order Traversal.
#Memory Usage: 14.1 MB, less than 50.12% of Python3 online submissions for Binary Tree Level Order Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return root
        depth = 0
        queue = {depth : [root]}
        result = []
        while queue:
            if not depth in queue:
                return result
            result.append([])
            for node in queue[depth]:
                result[depth].append(node.val)
                if node.left:
                    if depth+1 not in queue:
                        queue[depth+1] = [node.left]
                    else:
                        queue[depth+1].append(node.left)
                if node.right:
                    if depth+1 not in queue:
                        queue[depth+1] = [node.right]
                    else:
                        queue[depth+1].append(node.right)
            depth += 1
