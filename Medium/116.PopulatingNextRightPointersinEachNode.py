"""
    You are given a perfect binary tree where all leaves are on the same level, 
    and every parent has two children. The binary tree has the following 
    definition:

        struct Node {
          int val;
          Node *left;
          Node *right;
          Node *next;
        }
    Populate each next pointer to point to its next right node. If there is no 
    next right node, the next pointer should be set to NULL.
    Initially, all next pointers are set to NULL.

    Follow up:
        - You may only use constant extra space.
        - Recursive approach is fine, you may assume implicit stack space does 
          not count as extra space for this problem.

    Example:

                1                1 - NULL
               / \              / \
              2   3            2 - 3 - NULL
             / \ / \          / \ / \
            4  5 6  7        4--5-6--7 - NULL
    Input: root = [1,2,3,4,5,6,7]
    Output: [1,#,2,3,#,4,5,6,7,#]
    Explanation: Given the above perfect binary tree (Figure A), your function 
                 should populate each next pointer to point to its next right 
                 node, just like in Figure B. The serialized output is in level 
                 order as connected by the next pointers, with '#' signifying 
                 the end of each level.

    Constraints:
        - The number of nodes in the given tree is less than 4096.
        - -1000 <= node.val <= 1000
"""
#Difficulty: Medium
#58 / 58 test cases passed.
#Runtime: 76 ms
#Memory Usage: 15.1 MB

#Runtime: 76 ms, faster than 43.57% of Python3 online submissions for Populating Next Right Pointers in Each Node.
#Memory Usage: 15.1 MB, less than 96.92% of Python3 online submissions for Populating Next Right Pointers in Each Node.

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = [root]
        while queue:
            length = len(queue)
            level = []
            while length:
                node = queue.pop(0)
                level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                length -= 1
            l = len(level)
            for i in range(l):
                if i == l - 1:
                    level[i].next = None
                if i + 1 < l:
                    level[i].next = level[i+1]
        return root
