"""
Problem: 
    Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
    k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
    You may not alter the values in the list's nodes, only nodes themselves may be changed.

Test Cases:
    Example 1:
        Input: head = [1,2,3,4,5], k = 2
        Output: [2,1,4,3,5]
    Example 2:
        Input: head = [1,2,3,4,5], k = 3
        Output: [3,2,1,4,5]
"""

#Time: O(n)
#Space: O(1)

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #we need dummy node for odd number of lists and also keeps track of original head
        dummy = ListNode(0, head)

        groupPrev = dummy
        
        while True: 
            kth = self.getKth(groupPrev, k)
            #if there is no more room for next group(reached the end of list) then we break from our loop
            if not kth: 
                break

            groupNext = kth.next

            #reverse group
            prev, curr = kth.next, groupPrev.next 
            while curr != groupNext: 
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp 


        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0: 
            curr = curr.next 
            k -= 1

        return curr

    #1st iteration 
    #setting variables
    #groupPrev = dummy : kth = 2 : groupNext = 3 (kth(2).next)
    #Reverse list (while curr != groupNext)
    # prev = 3(kth(2).next), curr = 1 (groupPrev(dummy).next)
    #changing variables
    # tmp = 2 (curr.next), curr(1).next = 3(prev), prev(3) = 1(curr), curr(1) = 2(tmp) 
    #      c         p
    # none 2 -> 3    1 -> 3 -> 4 -> 5
    #second reverse iteration
    # tmp = 3(curr.next), curr(2).next = 1(prev), prev(1) = 2(curr), curr(2) = 3(tmp)
    #           pc          (curr = groupNext) exit loop
    # 2 -> 1 -> 3 -> 4 -> 5


    #After reverse
    # tmp = 1 (groupPrev(dummy).next), groupPrev(dummy).next = 2 (kth), groupPrev(dummy) = 1(tmp)
    # dummy -> 1   2 -> 1 -> 3 -> 4 -> 5  
    #                 groupPrev
    # dummy -> 2 -> 1 -> 3 -> 4 -> 5
