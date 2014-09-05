'''
We can convert the first part of the problem into a recurrence relation i.e. F(N) = F(N-1) + F(N-4) with the base case : F(0) = F(1) = F(2) = F(3) = 1. 
Here, F(N) represents the number of ways of tiling the 4xN rectangle with 4x1 and 1x4 tiles. The explanation goes as :
If we place a 4x1 tile, then we just need to solve for F(N-1).
If we place a 1x4 tile, then we can't place a 4x1 tile under it. Basically, we will have to place a set of four 1x4 tiles together, hence we solve forF(N-4).
'''
from math import sqrt

def generate_terms(series):
    # N<=40
    N = 4
    while N<=40:
        next_term = series[N - 1] + series[N - 4]
        series.append(next_term)
        N += 1

def generate_primes(M):
    max_number = M + 1
    primes = [True] * max_number
    primes[0] = primes[1] = False
    i = 2
    bound = int(sqrt(M+1))
    while (i <= bound):
        if primes[i]:
            n = 2
            j = n * i
            while j < len(primes):
                primes[j] = False
                n += 1
                j = n * i
        i += 1
    return primes
            
series = [1,1,1,1] #F0,1,2,3
generate_terms(series)
primes = generate_primes(series[40])

t = int(raw_input())
while t:
    t -= 1
    n = int(raw_input())
    # get configuration number
    M = series[n]
    # count primes <= M
    i = 2
    result = 0
    while i <= M:
        if primes[i]:
            result += 1
        i += 1
    print result
