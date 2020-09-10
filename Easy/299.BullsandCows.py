"""
    You are playing the following Bulls and Cows game with your friend: You 
    write down a number and ask your friend to guess what the number is. Each 
    time your friend makes a guess, you provide a hint that indicates how many 
    digits in said guess match your secret number exactly in both digit and 
    position (called "bulls") and how many digits match the secret number but 
    locate in the wrong position (called "cows"). Your friend will use 
    successive guesses and hints to eventually derive the secret number.
    Write a function to return a hint according to the secret number and 
    friend's guess, use A to indicate the bulls and B to indicate the cows. 
    Please note that both secret number and friend's guess may contain 
    duplicate digits.

    Example:
    Input: secret = "1807", guess = "7810"
    Output: "1A3B"
    Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.

    Example:
    Input: secret = "1123", guess = "0111"
    Output: "1A1B"
    Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is 
                 a cow.

    Note: You may assume that the secret number and your friend's guess only 
          contain digits, and their lengths are always equal.
"""
#Difficulty: Easy
#152 / 152 test cases passed.
#Runtime: 84 ms
#Memory Usage: 13.7 MB

#Runtime: 84 ms, faster than 12.39% of Python3 online submissions for Bulls and Cows.
#Memory Usage: 13.7 MB, less than 83.60% of Python3 online submissions for Bulls and Cows.

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret = list(secret)
        guess = list(guess)
        i, bulls, cows = 0, 0, 0
        l = len(secret)
        while i < l:
            if guess[i] == secret[i]:
                bulls += 1
                guess.pop(i)
                secret.pop(i)
                l = len(secret)
                continue
            i += 1
        i = 0
        while i < l:
            if guess[i] in secret:
                cows += 1
                secret.remove(guess[i])
                guess.pop(i)
                l = len(secret)
                continue
            i += 1
        return str(bulls) + 'A' + str(cows) + 'B'
