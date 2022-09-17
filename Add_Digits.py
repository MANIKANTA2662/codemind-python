n=int(input())
s=11
while 10<s:
    s=0
    while n>0:
        i=n%10
        s+=i
        n=n//10
    n=s
print(s)