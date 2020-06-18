
class NOD:
    def __init__(self, n):
        self.num = n

    def total_digits(self):
        c = 0
        if(self.num == 0):
            return 1
        while (self.num):
            a = self.num % 10
            c += 1
            self.num //= 10
        return c


n = int(input("\nPlease enter the number to check it's number of digits:\n"))
a = NOD(n)
print(f"{a.total_digits()}")
