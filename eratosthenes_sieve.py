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
        t0 = time() # exact time before algorithm start
        lst = [True] * (n-1) # generating array with bool values, default is "True"
        stop = round(sqrt(n)+0.5) # calculating id of last iterated element
        for i in range(2, stop): # first prime number is 2, stop iterating on "stop" 
            for j in range(i+i, n+1, i): # change every non prime to "False"
                lst[j-2] = False # indices start at 0, we started iterating with 2
        if f: # if chosen yes at start prints "stop" and all prime numbers 
            print('Stop iterating at', stop)
            for i in range(n-1):
                if lst[i]:
                    print(i+2, end=' ')
            print('')
        t1 = time() # exact time after algorithm ends
        print("Time required:", round(t1 - t0, 5), 'seconds') # execution time
