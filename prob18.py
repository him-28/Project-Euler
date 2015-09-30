import time
t = time.time()
 
row=[]
with open('18.txt','r') as f :
    for l in iter(f.readline, '') : row.append(map(int,l.rstrip().split(' ')))
 
while len(row[-1])>1 :
    for i in range(len(row[-2])):
        row[-2][i]+=row[-1][i] if row[-1][i]>row[-1][i+1] else row[-1][i+1]
    del row[-1]
 
print "\nans=%s\n\n%sms elapsed" % (row[0][0], (time.time()-t)*1000)
