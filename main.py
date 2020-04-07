from math import sqrt
from time import time


class GenPrimeList:

    def start(self):
        lim = input("input upper threshold: ")
        f = input("print all primes(y/n)? ")
        if f == 'n':
            f = 0
        while True:
            try:
                lim = int(lim)
                break
            except ValueError:
                print("incorrect input\n")
                lim = input("input upper threshold: ")
        self.sieve(int(lim), f)

    @staticmethod
    def sieve(n, f):
        t0 = time()
        lst = [True] * (n-1)
        stop = round(sqrt(n)+0.5)
        for i in range(2, stop):
            for j in range(i+i, n+1, i):
                lst[j-2] = False
        if f:
            print('Stop iterating at', stop)
            for i in range(n-1):
                if lst[i]:
                    print(i+2, end=' ')
            print('')
        t1 = time()
        print("Time required:", round(t1 - t0, 5), 'seconds')
