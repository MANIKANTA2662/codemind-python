n=int(input())
l=list(map(int,input().split()))
e=0
for i in range(1,len(l)-1):
    if(l[i]%2==1 and l[i-1]%2==1 and l[i+1]%2==1):
        e=e+1
print(e)