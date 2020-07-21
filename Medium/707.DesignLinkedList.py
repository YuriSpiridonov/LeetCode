"""
    Design your implementation of the linked list. You can choose to use the 
    singly linked list or the doubly linked list. A node in a singly linked 
    list should have two attributes: val and next. val is the value of the 
    current node, and next is a pointer/reference to the next node. If you want 
    to use the doubly linked list, you will need one more attribute prev to 
    indicate the previous node in the linked list. Assume all nodes in the 
    linked list are 0-indexed.

    Implement these functions in your linked list class:
        - get(index) : Get the value of the index-th node in the linked list. 
          If the index is invalid, return -1.
        - addAtHead(val) : Add a node of value val before the first element of 
          the linked list. After the insertion, the new node will be the first 
          node of the linked list.
        - addAtTail(val) : Append a node of value val to the last element of 
          the linked list.
        - addAtIndex(index, val) : Add a node of value val before the index-th 
          node in the linked list. If index equals to the length of linked list, 
          the node will be appended to the end of linked list. If index is 
          greater than the length, the node will not be inserted.
        - deleteAtIndex(index) : Delete the index-th node in the linked list, 
          if the index is valid.

    Example:
    Input: 
    ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
    [[],[1],[3],[1,2],[1],[1],[1]]
    Output:  
    [null,null,null,null,2,null,3]

    Explanation:
    MyLinkedList linkedList = new MyLinkedList(); // Initialize empty LinkedList
    linkedList.addAtHead(1);
    linkedList.addAtTail(3);
    linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
    linkedList.get(1);            // returns 2
    linkedList.deleteAtIndex(1);  // now the linked list is 1->3
    linkedList.get(1);            // returns 3

    Constraints:
        - 0 <= index,val <= 1000
        - Please do not use the built-in LinkedList library.
        - At most 2000 calls will be made to get, addAtHead, addAtTail, 
          addAtIndex and deleteAtIndex.
"""
#Difficulty: Medium
#57 / 57 test cases passed.
#Runtime: 300 ms
#Memory Usage: 14.3 MB

#Runtime: 300 ms, faster than 49.54% of Python3 online submissions for Design Linked List.
#Memory Usage: 14.3 MB, less than 63.36% of Python3 online submissions for Design Linked List.

class Node:

    def __init__(self, val):
        """
        Initialize of the Node.
        """
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(None)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is 
        invalid, return -1.
        """
        node = self.head
        for i in range(index):
            node = node.next
        return node.val if node else -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. 
        After the insertion, the new node will be the first node of the linked 
        list.
        """
        if self.head.val is not None:
            old_head = self.head
            self.head = Node(val)
            self.head.next = old_head
        else:
            self.head.val = val

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended 
        to the end of linked list. If index is greater than the length, the 
        node will not be inserted.
        """
        if index == 0:
            return self.addAtHead(val)
        prev = None
        for i in range(index):
            if prev:
                prev = prev.next
                next_node = next_node.next
            else:    
                prev = self.head
                next_node = self.head.next
        node = Node(val)
        prev.next = node
        node.next = next_node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            self.head = self.head.next
            return
        prev = None
        for i in range(index):
            if prev and next_node:
                if not next_node.next:
                    return
                prev = prev.next
                next_node = next_node.next
            else:
                prev = self.head
                next_node = self.head.next
        if next_node:
            prev.next = next_node.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
