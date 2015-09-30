import time
tStart = time.time()

values = 0

def factorial(x):
    y = 1
    for i in range(1,x+1):
        y = y * i
        
    return y

def calc(n, r):
    return  factorial(n) / (factorial(r) * factorial(n-r))

for i in range(1,101):
    for j in range(1, i):
        if calc(i, j) > 1000000:
            values += 1
           

print(values)
print("time:" + str(time.time() - tStart))
