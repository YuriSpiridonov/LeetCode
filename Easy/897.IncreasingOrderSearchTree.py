"""
    Given a binary search tree, rearrange the tree in in-order so that the 
    leftmost node in the tree is now the root of the tree, and every node has 
    no left child and only 1 right child.

    Example:
    Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

                   5
                  / \
                3    6
               / \    \
              2   4    8
             /        / \
            1        7   9

    Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

             1
              \
               2
                \
                 3
                  \
                   4
                    \
                     5
                      \
                       6
                        \
                         7
                          \
                           8
                            \
                             9

    Constraints:
        - The number of nodes in the given tree will be between 1 and 100.
        - Each node will have a unique integer value from 0 to 1000.
"""
#Difficulty: Easy
#35 / 35 test cases passed.
#Runtime: 24 ms
#Memory Usage: 14 MB

#Runtime: 24 ms, faster than 97.01% of Python3 online submissions for Increasing Order Search Tree.
#Memory Usage: 14 MB, less than 17.15% of Python3 online submissions for Increasing Order Search Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = []
        new_root = None
        while True:
            if root:
                stack.append(root)
                root = root.left
            elif stack:
                root = stack.pop()
                if not new_root:
                    new_root = root
                    new_node = new_root
                else:
                    new_node.right = root
                    new_node = new_node.right
                    new_node.left = None
                root = root.right
            else:
                break
        return new_root
