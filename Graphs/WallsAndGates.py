"""
Problem: 
    You are given an m x n grid rooms initialized with these three possible values.
        - -1 A wall or an obstacle.
        - 0 A gate.
        - INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the 
        distance to a gate is less than 2147483647.

    Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Test Cases:
    Example 1:
        Input: rooms = [
        [2147483647,-1,0,2147483647],
        [2147483647,2147483647,2147483647,-1],
        [2147483647,-1,2147483647,-1],
        [0,-1,2147483647,2147483647]]

        Output: [
        [3,-1,0,1],
        [2,2,1,-1],
        [1,-1,2,-1],
        [0,-1,3,4]]

    Example 2:
        Input: rooms = [[-1]]
        Output: [[-1]]
"""

# Time: O(m * n)
# Space: O(m * n)
# Where m is the number of rows and n is the number of columns in the grid

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = deque()

        # Function to add rooms to queue (if room not visited or a wall)
        def addRoom(r, c): 
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS
                or (r, c) in visit or rooms[r][c] == -1): 
                return

            q.append([r, c])
            visit.add((r, c))

        # Multisource BFS by added all positions with a gate to queue
        for r in range(ROWS):
            for c in range(COLS): 
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0

        while q:
            # Visit each adjacent room in the queue
            # and check if we can add room
            for i in range(len(q)): 
                r, c = q.popleft()
                rooms[r][c] = dist

                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            
            # Once we visited each adjacent room we can visit the room
            dist += 1 
            