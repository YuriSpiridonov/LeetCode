'''
    Given a binary tree root and a linked list with head as 
    the first node. 

    Return True if all the elements in the linked list 
    starting from the head correspond to some downward path 
    connected in the binary tree otherwise return False.

    In this context downward path means a path that starts 
    at some node and goes downwards.

    Example:
    Input: head = [4,2,8], 
           root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
    Output: true
    Explanation: Nodes in blue form a subpath in the binary 
                 Tree.  

    Example:
    Input: head = [1,4,2,6], 
           root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
    Output: true

    Example:
    Input: head = [1,4,2,6,8], 
           root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
    Output: false
    Explanation: There is no path in the binary tree that 
                 contains all the elements of the linked 
                 list from head.

    Constraints:
        - The number of nodes in the tree will be in the 
          range [1, 2500].
        - The number of nodes in the list will be in the 
          range [1, 100].
        - 1 <= Node.val <= 100 for each node in the linked 
          list and binary tree.
'''
#Difficulty: Medium
#67 / 67 test cases passed.
#Runtime: 200 ms
#Memory Usage: 16.1 MB

#Runtime: 200 ms, faster than 11.80% of Python3 online submissions for Linked List in Binary Tree.
#Memory Usage: 16.1 MB, less than 63.92% of Python3 online submissions for Linked List in Binary Tree.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        self.result = 0
        self.dfs(root, head)
        return self.result
    
    def dfs(self, root, head):
        if not root:
            return False
        if root.val == head.val:
            self.result = max(self.result, self.headFollower(root, head))
        self.dfs(root.left, head)
        self.dfs(root.right, head)
        
    def headFollower(self, root, head):
        if root.left and head.next and root.left.val == head.next.val and root.right and head.next and root.right.val == head.next.val:
            return max(self.headFollower(root.left, head.next), self.headFollower(root.right, head.next)) 
        
        if root.left and head.next and root.left.val == head.next.val:
            return self.headFollower(root.left, head.next)
        
        if root.right and head.next and root.right.val == head.next.val:
            return self.headFollower(root.right, head.next)
        
        return root.val == head.val and head.next == None