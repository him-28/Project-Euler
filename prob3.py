import math #for sqrt function
num = 600851475143
 
def isprime(x):
    for i in range(2,x):
        if x%i==0 : return False
    return True
 
root=int(math.sqrt(num))+1 #ignore factors larger than sqrt
 
#build array of factors
arr=[]
for i in range(1,root):
    if num%i == 0: arr.append(i)
 
#start at largest factor and remove if non-prime
arr.reverse()
for i in arr:
    if isprime(i): ans = i; break
 
print('largest prime factor: {0}'.format(ans))
