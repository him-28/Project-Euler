import math #for sqrt function
max = 2000000
p = [2] #primes
i=2
ans=p[0]

while (1) :
    if not i<max : break
    i+=1
    for j in p :
        if i%j==0 : break
        elif j==p[-1] or j>math.sqrt(i): p.append(i); ans+=i; break

print ans

