"""
    Design a simplified version of Twitter where users can post tweets, 
    follow/unfollow another user and is able to see the 10 most recent tweets 
    in the user's news feed. Your design should support the following methods:
    
    1. postTweet(userId, tweetId): Compose a new tweet.
    2. getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's 
       news feed. Each item in the news feed must be posted by users who the 
       user followed or by the user herself. Tweets must be ordered from most 
       recent to least recent.
    3. follow(followerId, followeeId): Follower follows a followee.
    4. unfollow(followerId, followeeId): Follower unfollows a followee.
    
    Example:
    
    Twitter twitter = new Twitter();
    // User 1 posts a new tweet (id = 5).
    twitter.postTweet(1, 5);
    // User 1's news feed should return a list with 1 tweet id -> [5].
    twitter.getNewsFeed(1);
    // User 1 follows user 2.
    twitter.follow(1, 2);
    // User 2 posts a new tweet (id = 6).
    twitter.postTweet(2, 6);
    // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
    // Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
    twitter.getNewsFeed(1);
    // User 1 unfollows user 2.
    twitter.unfollow(1, 2);
    // User 1's news feed should return a list with 1 tweet id -> [5],
    // since user 1 is no longer following user 2.
    twitter.getNewsFeed(1);
"""
#Difficulty: Medium
#23 / 23 test cases passed.
#Runtime: 548 ms
#Memory Usage: 20 MB

#Runtime: 548 ms, faster than 7.80% of Python3 online submissions for Design Twitter.
#Memory Usage: 20 MB, less than 5.26% of Python3 online submissions for Design Twitter.

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.feed = {}
        self.followers = {}
        self.time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.feed[self.time] = (userId, tweetId)
        self.time += 1
        
    def getNewsFeed(self, userId: int):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed.
        Each item in the news feed must be posted by users who the user
        followed or by the user herself.
        Tweets must be ordered from most recent to least recent.
        """
        news_feed = []
        time_line = sorted(self.feed.keys(), reverse = True)
        for time in time_line:
            current_user, tweet = self.feed[time]
            if current_user == userId or (userId in self.followers and current_user in self.followers[userId]):
                news_feed.append(tweet)
            if len(news_feed) == 10:
                break
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee.
        If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId:
            return
        if followerId in self.followers:
            self.followers[followerId].append(followeeId)
        else:
            self.followers[followerId] = [followeeId]
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee.
        If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId or followerId not in self.followers:
            return
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
