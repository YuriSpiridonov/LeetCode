"""
    Given a linked list, rotate the list to the right by k places, where k is 
    non-negative.

    Example:
    Input: 1->2->3->4->5->NULL, k = 2
    Output: 4->5->1->2->3->NULL
    Explanation:
                 rotate 1 steps to the right: 5->1->2->3->4->NULL
                 rotate 2 steps to the right: 4->5->1->2->3->NULL

    Example:
    Input: 0->1->2->NULL, k = 4
    Output: 2->0->1->NULL
    Explanation:
                 rotate 1 steps to the right: 2->0->1->NULL
                 rotate 2 steps to the right: 1->2->0->NULL
                 rotate 3 steps to the right: 0->1->2->NULL
                 rotate 4 steps to the right: 2->0->1->NULL
"""
#Difficulty: Medium
#231 / 231 test cases passed.
#Runtime: 28 ms
#Memory Usage: 14.1 MB

#Runtime: 28 ms, faster than 98.18% of Python3 online submissions for Rotate List.
#Memory Usage: 14.1 MB, less than 14.13% of Python3 online submissions for Rotate List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        index = 0
        node = head
        length = self.length(head)
        k = k % length
        if k != 0:
            while index + k < length:
                index += 1
                node = node.next
            return self.rotateFunc(node, head, index)
        else:
            return head
        
    def length(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def rotateFunc(self, head, tail, index):
        new_head = ListNode(head.val)
        head = head.next
        node = new_head
        while head:
            node.next = ListNode(head.val)
            node = node.next
            head = head.next
        while index > 0:
            node.next = ListNode(tail.val)
            node = node.next
            tail = tail.next
            index -= 1
        return new_head
