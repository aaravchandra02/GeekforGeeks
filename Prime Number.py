import time
import math


class solution:

    # O(n) for 1 number checking
    # O(n**2) for 'n' number checking
    def check_if_prime_naive(self, n):
        num = n
        if n == 0:
            return
        if n == 1:
            return True
        for i in range(2, num-1):
            if (num % i == 0):
                return False
        return True

    # Optimized version of the above problem.
    # O(n*root(n))
    def check_if_prime_root_n(self, n):
        """
        As the divisors of a num is in pair, if we search from 2 to root(n).
        """
        for i in range(2, math.floor(math.sqrt(n))):
            if (n % i == 0):
                return False
        return True

    """ O(m*n) - Sieve of Erastosthenes with starting point as the number**2.
    It is done based on the root(n) principle. It is futile running before n**2.
    """

    def check_if_prime_SoE(self, n):
        if(n < 2):
            print("Invalid input, try entering value greater than 1.\n")
            return
        l = [i for i in range(2, n+1)]
        # Going through each number.
        for i in l:
            """ Starting from square and adding the same number, 
            hence eliminating each multiple of a number till the inputted number.
            """
            for j in range(i**2, l[-1]+1, i):
                if(j in l[i:]):
                    l.remove(j)
                continue
        print(f"5\n{l}\n")


a = solution()
n = input(
    "Enter the positive number till which you want to find the prime numbers:\n")
a.check_if_prime_SoE(int(n))
