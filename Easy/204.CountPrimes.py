'''
    Count the number of prime numbers less than a non-negative 
    number, n.

    Example:
    Input: n = 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, 
                 they are 2, 3, 5, 7.

    Example:
    Input: n = 0
    Output: 0

    Example:
    Input: n = 1
    Output: 0

    Constraints:
        0 <= n <= 5 * 10^6
'''
#Difficulty: Easy
#21 / 21 test cases passed.
#Runtime: 1744 ms
#Memory Usage: 92.1 MB

#Runtime: 1744 ms, faster than 31.36% of Python3 online submissions for Count Primes.
#Memory Usage: 92.1 MB, less than 17.77% of Python3 online submissions for Count Primes.

class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [True] * n
        i = 2
        while i * i < n:
            if is_prime[i]:
                j = i * i
                while j < n:
                    is_prime[j] = False
                    j += i
            i += 1
        return sum(is_prime[2:])