"""
Problem: 
    The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
    Implement the MedianFinder class:

    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far. Answers within 10- of the actual answer will be accepted.

Test Cases: 
    Example 1:
        Input
        ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
        [[], [1], [2], [], [3], []]
        Output
        [null, null, null, 1.5, null, 2.0]

        Explanation
        MedianFinder medianFinder = new MedianFinder();
        medianFinder.addNum(1);    // arr = [1]
        medianFinder.addNum(2);    // arr = [1, 2]
        medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
        medianFinder.addNum(3);    // arr[1, 2, 3]
        medianFinder.findMedian(); // return 2.0
"""

# Time: O(m * log(n)) for addNum, O(m) for findMedian
# Space: O(n)
# Where m is the number of function calls and n is the length of the array

class MedianFinder:

    def __init__(self):
        # use 2 heaps to store values, max heap to store small vals, minHeap to store big values

        self.small = [] # small vals (max heap)
        self.large = [] # large vals (min heap)
        

    def addNum(self, num: int) -> None:
        # Nums in small must be less than or equal to nums in large heap
        # add to small heap by default but if difference is bigger than 2, then add to smaller heap
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num) # make negative for max heap
        
        # Heaps must be = or only differ by length of 1
        # when adding to heap, if heap length is greater than 2, pop from heap of greater
        # length and add to heap with shorter length

        if len(self.small) > len(self.large) + 1:
            # Pop from small heap
            smallVal = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, smallVal)

        if len(self.large) > len(self.small) + 1:
            # Pop from large heap
            largeVal = heapq.heappop(self.large)
            heapq.heappush(self.small, largeVal)

            

    def findMedian(self) -> float:
        # Do not use heappop to get vals since findMedian may be called
        # before adding another numer 
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0] 
        else:
            smallVal = -1 * self.small[0]
            largeVal = self.large[0] 
            return (smallVal + largeVal) / 2
