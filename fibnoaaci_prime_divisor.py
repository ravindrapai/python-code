from math import sqrt

def is_prime(n):
    max_limit = sqrt(n)
    i = 2
    while i <= max_limit:
        if n%i == 0:
            return False
        i += 1
    return True

def prime_divisors(y):
    i = 2
    result = []
    while (y != 1):
        if y%i == 0:
            y = y/i
            result.append(i) 
            print result
        else:
            i = i + 1
    print sum(set(result))
fib1 = 1
fib2 = 1
fib = []
while 1:
    next_fib = fib1 + fib2
    fib1, fib2 = fib2, next_fib
    if next_fib > 227000:
        if is_prime(next_fib):
            break
    fib.append(next_fib)
prime_fib = next_fib
Y = prime_fib + 1
print prime_fib, Y
prime_divisors(Y)
