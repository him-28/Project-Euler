from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    for i in xrange(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    else:
        return True


def is_circular_prime(m):
    m = str(m)
    total = [m[dex:] + m[:dex] for dex, number in enumerate(m)]
    return all([is_prime(int(k)) for k in total]) == True


count = 13
for x in xrange(100, 1000000):
    if not any(char in "02468" for char in str(x)) and is_circular_prime(x) == True:
        count += 1
print count
