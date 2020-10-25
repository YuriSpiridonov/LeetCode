"""
    Given a linked list, swap every two adjacent nodes and return its head.
    
    You may not modify the values in the list's nodes. Only nodes itself may 
    be changed.

    Example:
    1 -> 2 -> 3 -> 4
           V
    2 -> 1 -> 4 -> 3
    Input: head = [1,2,3,4]
    Output: [2,1,4,3]

    Example:
    Input: head = []
    Output: []

    Example:
    Input: head = [1]
    Output: [1]

    Constraints:
        - The number of nodes in the list is in the range [0, 100].
        - 0 <= Node.val <= 100
"""
#Difficulty: Medium
#55 / 55 test cases passed.
#Runtime: 28 ms
#Memory Usage: 14.2 MB

#Runtime: 28 ms, faster than 84.26% of Python3 online submissions for Swap Nodes in Pairs.
#Memory Usage: 14.2 MB, less than 99.98% of Python3 online submissions for Swap Nodes in Pairs.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd = head
        even = head.next
        if not even:
            return head
        else:
            new_head = ListNode(even.val)
            node = new_head
            node.next = ListNode(odd.val)
            node = node.next
        tail = even.next
        while tail:
            odd = tail
            tail = tail.next
            even = tail
            if tail:
                tail = tail.next
            if not even:
                node.next = ListNode(odd.val)
            else:
                node.next = ListNode(even.val)
                node = node.next
                node.next = ListNode(odd.val)
                node = node.next
        return new_head
