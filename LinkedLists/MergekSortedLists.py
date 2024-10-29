"""
Problems: 
    You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
    Merge all the linked-lists into one sorted linked-list and return it.
Test Cases: 
    Example 1:
        Input: lists = [[1,4,5],[1,3,4],[2,6]]
        Output: [1,1,2,3,4,4,5,6]
        Explanation: The linked-lists are:
        [
        1->4->5,
        1->3->4,
        2->6
        ]
        merging them into one sorted list:
        1->1->2->3->4->4->5->6
    Example 2:
        Input: lists = []
        Output: []
    Example 3:
        Input: lists = [[]]
        Output: []
"""

#Time: O(n * log(k)) where n is the total number of lists and k is the amount of times we have to merge k lists (we are halving the amount of) 
#lists we have to merge each time we merge so Log(k)
#Space: O(1)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0: 
            return None

        #greater than 1 because we want pairs 
        while len(lists) > 1:
            mergedList = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedList.append(self.mergeList(l1, l2)) #taking pairs of linked lists from array and sorting

                #first iteration (For loop)
                #merging [1,4,5] and [1,3,4] into [1,1,3,4,4,5]
                #mergedList = [[1,1,3,4,4,5]]
                #second iteration (i = 2)
                #merging [2,6] and None into [2,6]
                #lists = [[1,1,3,4,4,5], [2,6]]
                #Then we update lists to mergedLists and then go through the while loop one more time
            lists = mergedList

        #By the end the Linked List should be at the first index
        return lists[0]

    def mergeList(self, l1, l2): 
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else: 
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next

        curr.next = l1 if l1 else l2

        return dummy.next
        