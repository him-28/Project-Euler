from math import sqrt
  
def d(n):
  s = 1
  t = sqrt(n)
  for i in range(2, int(t)+1):
    if n % i == 0: s += i + n / i
  if t == int(t): s -= t
  return s
 
sum = 0
abundant_numbers = set()
for i in range(1, 28123):
    if d(i) > i:
        abundant_numbers.add(i)
    if not any((i-a in abundant_numbers) for a in abundant_numbers):
        sum += i
print sum
