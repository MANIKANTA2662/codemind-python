a,b,d=map(int,input().split())
c=0
for i in range(a,b+1):
    if(i%d==0):
        c=c+1
print(c)
    
