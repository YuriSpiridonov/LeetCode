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
#Runtime: 48 ms
#Memory Usage: 15.3 MB

#Runtime: 48 ms, faster than 30.10% of Python3 online submissions for Reverse Linked List.
#Memory Usage: 15.3 MB, less than 60.64% of Python3 online submissions for Reverse Linked List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        next_element = None
        while current:
            next_element = current.next
            current.next = prev
            prev = current
            current = next_element
        return prev
