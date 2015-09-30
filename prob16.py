import time; t = time.time()
 
sum=0
for x in str(2**1000): sum+=int(x)
 
print "ans=%s\n\n%sms elapsed" % (sum, 1000*(time.time()-t))

