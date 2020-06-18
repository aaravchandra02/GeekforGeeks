import math
import time


class NOD:
    def __init__(self, n):
        self.num = abs(n)

    # O(digits)
    def total_digits_iterative(self):
        c = 0
        n = self.num
        if(n == 0):
            return 1
        while (n):
            a = n % 10
            c += 1
            n //= 10
        return c

    # O(digits)
    def total_digits_maths(self):
        return(math.floor(math.log10(self.num)+1))


n = int(input("\nPlease enter the number to check it's number of digits:\n"))
a = NOD(n)
start_time = time.time()
ans = a.total_digits_iterative()
end_time = time.time()
t = end_time-start_time
print(f"{ans} digits\t in {t}")

start_time = time.time()
ans = a.total_digits_maths()
end_time = time.time()
t = end_time-start_time
print(f"{ans} digits\t in {t}")
