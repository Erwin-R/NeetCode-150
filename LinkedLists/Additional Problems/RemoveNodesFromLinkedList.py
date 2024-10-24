"""
Problem: 
    You are given the head of a linked list.
    Remove every node which has a node with a greater value anywhere to the right side of it.
    Return the head of the modified linked list.

Test Cases:
    Example 1:
        Input: head = [5,2,13,3,8]
        Output: [13,8]
        Explanation: The nodes that should be removed are 5, 2 and 3.
        - Node 13 is to the right of node 5.
        - Node 13 is to the right of node 2.
        - Node 8 is to the right of node 3.
    Example 2:
        Input: head = [1,1,1,1]
        Output: [1,1,1,1]
        Explanation: Every node has value 1, so no nodes are removed.
"""

#Time: O(n) where n is the size of the linked list
#Space: O(1)


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev, curr = None, head
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev

        head = reverse(head)

        curr = head
        curMax = curr.val
        #since we are starting at the end of a linked list we know that there are not going to be any 
        #values greater to the right of curr
        while curr.next:
            if curr.next.val < curMax: 
                curr.next = curr.next.next
            else: 
                curMax = curr.next.val
                curr = curr.next
        
        return reverse(head)