"""
Count the number of prime numbers less than a non-negative 
number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they 
are 2, 3, 5, 7.
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3: 
            return 0

        prime = [True] * n
        prime[0] = prime[1] = False
        for i in range(2, n):
            if prime[i]:
                t = 2 * i
                while t < n:
                    prime[t] = False
                    t += i

        return sum(prime)
