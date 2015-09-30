fn = '13.txt' #filename
format= 'r' #read
file = open(fn,format)
 
nums=[]
for line in file : # iterate over each line
    if line is '' : break #quit when the line is empty (eof)
    nums.append(str(line).rstrip()) #force string, remove the newline char, stick in in my array
 
sum=0
for num in nums :
    sum+=int(num) #add each element of my array to a running total
 
sum = str(sum)[0:10] #toss unnecessary data
print sum
