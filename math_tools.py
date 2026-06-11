import random

# mod pow
def modular_pow(x, a, n):
    # check 1
    if n == 1:
        return 0
    # start 1
    result = 1
    # mod base
    x = x % n
    # loop bits
    while a > 0:
        # multiply if 1
        if a & 1:
            result = (result * x) % n
        # shift
        a >>= 1
        # square
        x = (x * x) % n
    return result

# egcd
def egcd(a, b):
    # base
    if a == 0:
        return (b, 0, 1)
    else:
        # recurse
        g, y, x = egcd(b % a, a)
        # return
        return (g, x - (b // a) * y, y)

# mod inverse
def modinv(a, m):
    # get gcd
    g, x, _ = egcd(a, m)
    # check if no inv
    if g != 1:
        print("Error: modular inverse does not exist")
        import sys
        sys.exit()
    return x % m

# split n-1
def try_decompose(n):
    # count 2s
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    return d, s

# check prime
def is_probable_prime(n, k=20):
    # check small
    if n < 2:
        return False
    # small primes
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for p in small_primes:
        if n % p == 0:
            return n == p

    # get d s
    d, s = try_decompose(n)

    # test k times
    for _ in range(k):
        # random base
        a = random.randint(2, n - 2)
        # test pow
        x = modular_pow(a, d, n)
        # check pass
        if x == 1 or x == n - 1:
            continue
        # square up
        composite = True
        for _r in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                composite = False
                break
        # return false if composite
        if composite:
            return False
    # probably prime
    return True

# get rand digits
def rand_by_digits(digits):
    # check valid
    if digits <= 0:
        print("Error: digits must be positive")
        import sys
        sys.exit()
    # get bounds
    low = 10 ** (digits - 1)
    high = 10 ** digits - 1
    # return rand
    return random.randint(low, high)

# make prime
def generate_prime(digits, k=20):
    # handle 1 digit
    if digits == 1:
        for p in [2, 3, 5, 7]:
            if is_probable_prime(p):
                return p
    # loop till prime
    while True:
        # get rand
        n = rand_by_digits(digits)
        # make odd
        if n % 2 == 0:
            n += 1
        # check prime
        if is_probable_prime(n, k=k):
            return n