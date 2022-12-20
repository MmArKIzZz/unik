s=[int(a) for a in input().split()]
f=[]
for i in range (len(s)):
    if int(s[i])%2!=0:
        f.append(s[i])

print(f)