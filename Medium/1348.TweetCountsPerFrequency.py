"""
    Implement the class TweetCounts that supports two methods:

    1. recordTweet(string tweetName, int time)
        - Stores the tweetName at the recorded time (in seconds).
    2. getTweetCountsPerFrequency(string freq, string tweetName, int startTime, 
       int endTime)
        - Returns the total number of occurrences for the given tweetName per 
          minute, hour, or day (depending on freq) starting from the startTime 
          (in seconds) and ending at the endTime (in seconds).
        - freq is always minute, hour or day, representing the time interval to 
          get the total number of occurrences for the given tweetName.
        - The first time interval always starts from the startTime, so the time 
          intervals are [startTime, startTime + delta*1>,  
          [startTime + delta*1, startTime + delta*2>, 
          [startTime + delta*2, startTime + delta*3>, ... , 
          [startTime + delta*i, min(startTime + delta*(i+1), endTime + 1) > 
          for some non-negative number i and delta (which depends on freq).  

    Example:
    Input
    ["TweetCounts","recordTweet", "recordTweet", "recordTweet", "getTweetCountsPerFrequency", "getTweetCountsPerFrequency", "recordTweet",  "getTweetCountsPerFrequency"]
    [[],          ["tweet3",0],  ["tweet3",60], ["tweet3",10], ["minute","tweet3",0,59],     ["minute","tweet3",0,60],     ["tweet3",120], ["hour","tweet3",0,210]      ]

    Output
    [null,null,null,null,[2],[2,1],null,[4]]

    Explanation
    TweetCounts tweetCounts = new TweetCounts();
    
    tweetCounts.recordTweet("tweet3", 0);
    tweetCounts.recordTweet("tweet3", 60);
    tweetCounts.recordTweet("tweet3", 10);                             
    // ^- All tweets correspond to "tweet3" with recorded times at 0, 10 and 60.
    
    tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59); 
    // ^- return [2]. The frequency is per minute (60 seconds), so there is one 
    //    interval of time: 1) [0, 60> - > 2 tweets.
    
    tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60); 
    // ^- return [2, 1]. The frequency is per minute (60 seconds), so there are 
    //    two intervals of time: 1) [0, 60> - > 2 tweets, and 2) [60,61> - > 1 tweet.
    
    tweetCounts.recordTweet("tweet3", 120);                            
    // ^- All tweets correspond to "tweet3" with recorded times at 0, 10, 60 and 120.
    
    tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210);  
    // ^- return [4]. The frequency is per hour (3600 seconds), so there is one 
    //    interval of time: 1) [0, 211> - > 4 tweets.

    Constraints:
        - There will be at most 10000 operations considering both recordTweet 
          and getTweetCountsPerFrequency.
        - 0 <= time, startTime, endTime <= 10^9
        - 0 <= endTime - startTime <= 10^4
"""
#Difficulty: Medium
#21 / 21 test cases passed.
#Runtime: 8576 ms
#Memory Usage: 35.8 MB

#Runtime: 8576 ms, faster than 5.30% of Python3 online submissions for Tweet Counts Per Frequency.
#Memory Usage: 35.8 MB, less than 5.77% of Python3 online submissions for Tweet Counts Per Frequency.

class TweetCounts:

    def __init__(self):
        self.tweetsDB = {}
        self.frequencyDB = {}
        self.second = 1
        self.minute = self.second * 60
        self.hour = self.minute * 60
        self.day = self.hour * 24
        self.time = {
            'minute' : self.minute,
            'hour' : self.hour,
            'day' : self.day
            }

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName in self.tweetsDB:
            self.tweetsDB[tweetName].append(time)
        else:
            self.tweetsDB[tweetName] = [time]

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        result = []
        i = count = 0
        timeLine = (startTime, endTime + 1)
        self.frequencyDB[timeLine] = []
        
        """
        Recive and sort all tweet time.
        """
        if tweetName in self.tweetsDB:
            tweetsTimes = sorted(self.tweetsDB[tweetName])
        
        """
        Figure out frequency of tweets.
        """
        if freq in self.time:
            freq = self.time[freq]
            numberOfTimeSequence = (endTime - startTime) // freq
        
        """
        Split time line into parts.
        """
        while i <= numberOfTimeSequence:
            self.frequencyDB[(startTime, endTime + 1)].append((startTime + freq * i, min(startTime + freq * (i+1), endTime + 1)))
            i += 1
        
        """
        Count tweets in every time line parts.
        """
        for time in self.frequencyDB[timeLine]:
            for tweetsTime in tweetsTimes:
                if time[0] <= tweetsTime < time[1]:
                    count += 1
            result.append(count)
            count = 0
        return result

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
