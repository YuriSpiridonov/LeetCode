"""
    A binary tree is named Even-Odd if it meets the following conditions:
        - The root of the binary tree is at level index 0, its children are at 
          level index 1, their children are at level index 2, etc.
        - For every even-indexed level, all nodes at the level have odd integer 
          values in strictly increasing order (from left to right).
        - For every odd-indexed level, all nodes at the level have even integer 
          values in strictly decreasing order (from left to right).

    Given the root of a binary tree, return true if the binary tree is Even-Odd, 
    otherwise return false.

    Example:
                1           - level 0
              /   \
            10     4        - level 1
           /      / \
          3      7   9      - level 2
         / \    /     \
       12   8  6       2    - level 3

    Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
    Output: true
    Explanation: The node values on each level are:
                 Level 0: [1]
                 Level 1: [10,4]
                 Level 2: [3,7,9]
                 Level 3: [12,8,6,2]
                 Since levels 0 and 2 are all odd and increasing, and levels 1 
                 and 3 are all even and decreasing, the tree is Even-Odd.

    Example:
                1           - level 0
              /   \
             4     2        - level 1
            / \   /
           3   3 7          - level 2

    Input: root = [5,4,2,3,3,7]
    Output: false
    Explanation: The node values on each level are:
                 Level 0: [5]
                 Level 1: [4,2]
                 Level 2: [3,3,7]
                 Node values in the level 2 must be in strictly increasing 
                 order, so the tree is not Even-Odd.

    Example:
                5           - level 0
              /   \
             9     1        - level 1
            / \   /
           3   5 7          - level 2    

    Input: root = [5,9,1,3,5,7]
    Output: false
    Explanation: Node values in the level 1 should be even integers.

    Example:
    Input: root = [1]
    Output: true

    Example:
    Input: root = [11,8,6,1,3,9,11,30,20,18,16,12,10,4,2,17]
    Output: true

    Constraints:
        - The number of nodes in the tree is in the range [1, 105].
        - 1 <= Node.val <= 106
"""
#Difficulty: Medium
#105 / 105 test cases passed.
#Runtime: 476 ms
#Memory Usage: 40.4 MB

#Runtime: 476 ms, faster than 90.99% of Python3 online submissions for Even Odd Tree.
#Memory Usage: 40.4 MB, less than 98.26% of Python3 online submissions for Even Odd Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        level = -1
        queue = [root]
        while queue:
            level += 1
            prev = None
            length = len(queue)
            while length:
                length -= 1
                node = queue.pop(0)
                if level % 2:
                    if node.val % 2 or prev and prev <= node.val:
                        return False
                else:
                    if not node.val % 2 or prev and prev >= node.val:
                        return False
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                prev = node.val
        return True
