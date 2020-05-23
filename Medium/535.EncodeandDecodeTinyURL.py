"""
    Note: This is a companion problem to the System Design problem: 
    Design TinyURL.
    TinyURL is a URL shortening service where you enter a URL such as 
    https://leetcode.com/problems/design-tinyurl and it returns a short URL 
    such as http://tinyurl.com/4e9iAk.
    
    Design the encode and decode methods for the TinyURL service. 
    There is no restriction on how your encode/decode algorithm should work. 
    You just need to ensure that a URL can be encoded to a tiny URL and the 
    tiny URL can be decoded to the original URL.
"""
#Difficulty: Medium
#739 / 739 test cases passed.
#Runtime: 28 ms
#Memory Usage: 13.7 MB

#Runtime: 28 ms, faster than 89.22% of Python3 online submissions for Encode and Decode TinyURL.
#Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Encode and Decode TinyURL.

import random
class Codec:

    def __init__(self):
        self.db = {}
        self.tiny = ''
        self.chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while len(self.tiny) < 7:
            self.tiny += self.chars[random.randint(0,61)]
            if len(self.tiny) == 6:
                if self.tiny not in self.db.keys():
                    self.db[self.tiny] = longUrl
                    return 'http://tinyurl.com/' + self.tiny
                else:
                    self.tiny = ''

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl[-6:] in self.db.keys():
            return self.db[shortUrl[-6:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
