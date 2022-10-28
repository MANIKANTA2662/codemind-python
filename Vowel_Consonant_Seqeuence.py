ss=input()
v='aeiou'
s=""
for i in ss:
    if i in v:
        s=s+"V"
    else:
        s=s+"C"
c=0
v=0
k=[]
for i in s:
    if i=="C":
        c=c+1
        v=v-v
        if c==1:
            k.append("C")
    else:
        v=v+1
        c=c-c
        if v==1:
            k.append("V")
            
for i in k:
    print(i,end="")