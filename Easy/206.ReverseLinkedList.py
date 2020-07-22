"""
    Reverse a singly linked list.

    Example:
    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL

    Follow up:
    A linked list can be reversed either iteratively or recursively. Could you 
    implement both?
"""
#Difficulty: Easy
#27 / 27 test cases passed.
#Runtime: 720 ms
#Memory Usage: 16.2 MB

#Runtime: 720 ms, faster than 5.95% of Python3 online submissions for Reverse Linked List.
#Memory Usage: 16.2 MB, less than 24.09% of Python3 online submissions for Reverse Linked List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        new_head = ListNode(stack.pop())
        while stack:
            self.addAtTail(new_head, stack.pop())
        return new_head

    def addAtTail(self, node, val):
        while node.next:
            node = node.next
        node.next = ListNode(val)
