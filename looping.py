import math
n=150
a=sum([i for i in range(1, n+1)]) #sum of 1 to n
b=sum([i for i in range(2, n+1,2)]) #even sum
c=sum([int(i) for i in str(n)])
d=math.log10(n)
print(a,b,c,d)
print(round(a+b+c+d))
    
