p,r,t=map(int,input().split())
m=pow((1+r/100),t)
ci=m*p
print(format(ci,".2f"))