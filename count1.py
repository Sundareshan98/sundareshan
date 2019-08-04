a1=int(input())
a=list(input().split())
l=[]
b=set(a)
b=list(b)
for i in range(0,len(b)):
    b1=a.count(b[i])
    if b1>1:
        l.append(b[i])
        
    else:
        continue
l1=sorted(l)
print(*l1)
