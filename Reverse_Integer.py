m=int(input())
k=[]
n=abs(m)
for i in range(len(str(n))):
    r=n%10
    n=n//10
    if(r!=0):
        k.append(r)
if(m>0):
   for i in k:
       print(i,end="")
elif(m<0):
    print("-",end="")
    for i in k:
        print(i,end="")