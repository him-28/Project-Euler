import math #for sqrt function
 
def divs(x) :
    num=0
    for i in range(1,int(math.sqrt(x))+1) :
        if x%i==0 : num+=2
    if math.sqrt(x)==int(math.sqrt(x)) : num+=1
    return num
 
def solve(x) :
    i=0; tri=0
    while(1) :
        i+=1; tri+=i
        if divs(tri)>x : return tri
 
print solve(500)
