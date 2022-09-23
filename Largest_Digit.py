n=int(input())
l=[]
while n>0:
    m=n%10
    l.append(m)
    n=n//10
print(max(l))
    
