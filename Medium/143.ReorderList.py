"""
    Given a singly linked list L: L0→L1→…→Ln-1→Ln,
    reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

    You may not modify the values in the list's nodes, only nodes itself may 
    be changed.

    Example:
    Given 1->2->3->4, reorder it to 1->4->2->3.

    Example:
    Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""
#Difficulty: Medium
#13 / 13 test cases passed.
#Runtime: 132 ms
#Memory Usage: 23.1 MB

#Runtime: 132 ms, faster than 30.76% of Python3 online submissions for Reorder List.
#Memory Usage: 23.1 MB, less than 79.26% of Python3 online submissions for Reorder List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        node = head
        while node:
            stack.append(node.val)
            node = node.next
        while stack:
            head.val = stack.pop(0)
            head = head.next
            if stack:
                head.val = stack.pop()
                head = head.next
