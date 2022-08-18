t=int(input())
j=0
for i in range(t):
    x=input()
    
    if(x=='++x' or x=='++X' or x=='x++' or x=='X++'):
        j=j+1
    else:
        j=j-1
print(j)