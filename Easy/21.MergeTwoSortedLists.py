'''
    Merge two sorted linked lists and return it as a new sorted 
    list. The new list should be made by splicing together the 
    nodes of the first two lists.

    Example:
    Input: l1 = [1,2,4], l2 = [1,3,4]
    Output: [1,1,2,3,4,4]

    Example:
    Input: l1 = [], l2 = []
    Output: []

    Example:
    Input: l1 = [], l2 = [0]
    Output: [0]

    Constraints:
        - The number of nodes in both lists is in the range 
          [0, 50].
        - -100 <= Node.val <= 100
        - Both l1 and l2 are sorted in non-decreasing order.
'''
#Difficulty: Easy
#208 / 208 test cases passed.
#Runtime: 40 ms
#Memory Usage: 14.3 MB

#Runtime: 40 ms, faster than 40.63% of Python3 online submissions for Merge Two Sorted Lists.
#Memory Usage: 14.3 MB, less than 26.66% of Python3 online submissions for Merge Two Sorted Lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1 = l1
        node2 = l2
        l3 = ListNode()
        node = l3
        while node:
            if node1 and node2 and node1.val > node2.val:
                node.next = node2
                node2 = node2.next
            elif node1:
                node.next = node1
                node1 = node1.next
            elif node2:
                node.next = node2
                node2 = node2.next
            node = node.next
        return l3.next
