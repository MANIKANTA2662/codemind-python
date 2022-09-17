n=int(input())
p=1
s=0
while n>0:
    i=n%10
    s+=i
    p*=i
    n=n//10
print(p-s)