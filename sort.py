a=int(input())
l=""
s1=""
for i in range(0,a):
    a=str(input())
    l+=a
s=sorted(l)
for i in range(0,len(s)):
    if s[i]==" ":
        continue
    else:
        s1+=s[i]
print(s1)

