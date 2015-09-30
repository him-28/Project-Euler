import time
t = time.time()*1000 #ms
 
max=20
set=[[1]]
 
print '\n'
 
for i in range(max) :
    set.append([1])
    while len(set[-1]) < len(set[-2]) :
        set[-1].append(set[-2][len(set[-1])]+set[-1][len(set[-1])-1])
    set[-1].append(2*set[-1][-1])
 
print "\nans={0}\n\n{1}ms elapsed".format(set[-1][-1], round(time.time()*1000-t, 3))

