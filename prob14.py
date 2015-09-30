import time
t = time.time()
 
max = 1000000
a=[]
for x in range(max) : a.append(int(0))
a[1]=1
ans=[0,0] #index, chain length
 
for i in range(2,max) :
    len,x = 0,i
    while x>1 : x = (x*3)+1 if x%2==1 else x/2; len+=1
    a[i] = len
 
for x in range(max) :
    if a[x] > ans[1] : ans = [x, a[x]]
print 'ans={0} (length={1})\n\n{2}s elapsed'.format(ans[0], ans[1], round(time.time()-t, 3))

