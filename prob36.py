def is_palindrome(i):
    i = str(i)
    return i == i[::-1]


def bin_palindrome(j):
    j = bin(j)
    return j[2:] == j[2:][::-1]


palindrome_sum = 0
for x in xrange(1, 1000000):
    if is_palindrome(x) == True and bin_palindrome(x) == True:
        palindrome_sum += x
print palindrome_sum
