from math import factorial

result = []
for x in xrange(1, 50000):
    total = []
    for y in str(x):
        total.append(factorial(int(y)))
    if sum(total) == x and sum(total) > 2:
        result.append(x)
print sum(result)
