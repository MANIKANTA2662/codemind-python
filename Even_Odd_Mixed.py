n=int(input())
c1=c2=0
while n>0:
    i=n%10
    if i%2==0:
        c1+=1
    else:
        c2+=1
    n//=10
if c1>0 and c2>0:
    print('Mixed')
elif c1==0 and c2>0:
    print('Odd')
else:
    print('Even')