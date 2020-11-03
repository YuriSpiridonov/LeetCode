"""
    Given the head of a linked list, return the list after sorting it in 
    ascending order.

    Follow up: Can you sort the linked list in O(n logn) time and O(1) memory 
    (i.e. constant space)?

    Example:
    nput: head = [4,2,1,3]
    Output: [1,2,3,4]

    Example:
    Input: head = [-1,5,3,4,0]
    Output: [-1,0,3,4,5]

    Example:
    Input: head = []
    Output: []

    Constraints:
        - The number of nodes in the list is in the range [0, 5 * 10**4].
        - -10**5 <= Node.val <= 10**5
"""
#Difficulty:
#28 / 28 test cases passed.
#Runtime: 220 ms
#Memory Usage: 37.8 MB

#Runtime: 220 ms, faster than 66.14% of Python3 online submissions for Sort List.
#Memory Usage: 37.8 MB, less than 6.25% of Python3 online submissions for Sort List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return
        current = head
        values = []
        while current:
            values.append(current.val)
            current = current.next
        values.sort(reverse=True)
        head = ListNode(values.pop())
        node = head
        while values:
            node.next = ListNode(values.pop())
            node = node.next
        return head
