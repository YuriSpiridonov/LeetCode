'''
    Given a singly linked list, group all odd nodes together 
    followed by the even nodes. Please note here we are 
    talking about the node number and not the value in the 
    nodes.

    You should try to do it in place. The program should run 
    in O(1) space complexity and O(nodes) time complexity.

    Example:
    Input: 1->2->3->4->5->NULL
    Output: 1->3->5->2->4->NULL

    Example:
    Input: 2->1->3->5->6->4->7->NULL
    Output: 2->3->6->7->1->5->4->NULL

    Constraints:
        - The relative order inside both the even and odd 
          groups should remain as it was in the input.
        - The first node is considered odd, the second node 
          even and so on ...
        - The length of the linked list is between [0, 10^4].
'''
#Difficulty: Medium
#71 / 71 test cases passed.
#Runtime: 40 ms
#Memory Usage: 16.3 MB

#Runtime: 40 ms, faster than 81.51% of Python3 online submissions for Odd Even Linked List.
#Memory Usage: 16.3 MB, less than 51.50% of Python3 online submissions for Odd Even Linked List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        i = 0
        odd = ListNode()
        even = ListNode()
        odd_node = odd
        even_node = even
        while head:
            if not i % 2:
                odd_node.next = head
                odd_node = odd_node.next
            else:
                even_node.next = head
                even_node = even_node.next
            i += 1
            head = head.next
        odd_node.next = even.next
        even_node.next = None
        return odd.next
