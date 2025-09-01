"""
Problem:
    You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.
    Return the minimum number of CPU intervals required to complete all tasks.

Test Cases:
    Example 1:
        Input: tasks = ["A","A","A","B","B","B"], n = 2
        Output: 8
        Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
        After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

    Example 2:
        Input: tasks = ["A","C","A","B","D","B"], n = 1
        Output: 6
        Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
        With a cooling interval of 1, you can repeat a task after just one other task.

    Example 3:
    Input: tasks = ["A","A","A", "B","B","B"], n = 3
    Output: 10
    Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
    There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.
"""

# Time: O(n) where n is the numbers of tasks 
# Space: O(1) since we have at most 26 different characters

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count number of letters in tasks array
        count = Counter(tasks)

        # Create maxHeap to track letter with most occurences
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        # Use a deque to track when you can add a letter again after n time (currCount, time)
        q = deque()
        time = 0


        while maxHeap or q:
            # increment time
            time += 1 

            # Check that maxHeap is non-empty
            if maxHeap:
                # Get count of letter and decrement
                cnt = 1 + heapq.heappop(maxHeap)

                # Add count to queue if not zero
                if cnt:
                    q.append([cnt, time + n])

            # Add num back to heap if time == q time
            # Check that q is non empty
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
