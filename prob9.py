import math

def solve(target):
    for a in range(1,target):
        for b in range(1,target-a):
            c = 1000 - a - b
            if c == math.sqrt(a**2+b**2) : return a*b*c

print solve(1000)
