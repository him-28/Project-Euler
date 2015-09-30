import itertools
print list(map("".join, itertools.permutations('0123456789')))[999999]
