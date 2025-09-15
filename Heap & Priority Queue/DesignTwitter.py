"""
Problem:
    Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

    Implement the Twitter class:

    Twitter() Initializes your twitter object.
    void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
    List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
    void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
    void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
    
Test Cases:
    Example 1:
        Input
        ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
        [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
        Output
        [null, null, [5], null, null, [6, 5], null, [5]]

        Explanation
        Twitter twitter = new Twitter();
        twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
        twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
        twitter.follow(1, 2);    // User 1 follows user 2.
        twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
        twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
        twitter.unfollow(1, 2);  // User 1 unfollows user 2.
        twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
"""

# Time: O(n log n) for each getNewsFeed() and O(1) for remaining methods
# Space: O(N * m + N * M + n)

# Where n is the total number of followeeIds associated with userId, m is the maximum number of tweets
# by any user, N is the total number of userIds and M is the maximum number of followees for any user
class Twitter:

    def __init__(self):
        # Map to hold set of followee followers 
        self.followMap = defaultdict(set)

        # Map to hold tweets of user with list storing last tweets
        self.tweetMap = defaultdict(list)

        # count to to hold most recent tweet (use negative numbers)
        self.count = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count, tweetId))
        self.count -= 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap =[]

        # Get all tweets from userId (includes all posts from user and who they are following)
        self.followMap[userId].add(userId)

        # get following and get their tweets 
        for followeeId in self.followMap[userId]:

            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]

                maxHeap.append([count, followeeId, tweetId, index - 1])

        heapq.heapify(maxHeap)
        
        while maxHeap and len(res) < 10:
            count, followeeId, tweetId, index = heapq.heappop(maxHeap)
            res.append(tweetId)
            
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId]
                heapq.heappush(maxHeap, [count, followeeId, tweetId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)