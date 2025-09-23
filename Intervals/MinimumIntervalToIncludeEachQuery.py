"""
Problem: 
    You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and 
    ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

    You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that 
    lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

    Return an array containing the answers to the queries.

Test Cases: 

    Example 1:
        Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
        Output: [3,3,1,4]
        Explanation: The queries are processed as follows:
        - Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
        - Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
        - Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
        - Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.

        
    Example 2:
        Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
        Output: [2,-1,4,6]
        Explanation: The queries are processed as follows:
        - Query = 2: The interval [2,3] is the smallest interval containing 2. The answer is 3 - 2 + 1 = 2.
        - Query = 19: None of the intervals contain 19. The answer is -1.
        - Query = 5: The interval [2,5] is the smallest interval containing 5. The answer is 5 - 2 + 1 = 4.
        - Query = 22: The interval [20,25] is the smallest interval containing 22. The answer is 25 - 20 + 1 = 6.
"""

# Time: O(n log(n) + m log(m))
# Space: O(n + m)

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        # Use heap to sort smallest interval for query (intervalLength, rightMostIntervalVal)
        minHeap = []

        # Map q to interval length {q : intervalLenght}
        res, i = {}, 0

        # Does not actually sort queries array but creates copy and iterates through sorted copy
        for q in sorted(queries): 
            
            # Push valid intervals for query into minHeap
            # Iterate through as long as long as start of interval is < query val (within interval range)
            while i < len(intervals) and intervals[i][0] <= q: 
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            # Pop invalid intervals from minHeap (If query > rightMost minInterval val)
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            # At this point you should have valid intervals in minHeap so add it to res map
            # check for edge case if minHeap is empty (no valid interval) so -1 
            res[q] = minHeap[0][0] if minHeap else -1

        return [res[q] for q in queries]
