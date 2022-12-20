s=[int(a) for a in input().split()]
f=[]
for i in range (len(s)-1):
    if int(s[i])<int(s[i+1]):
        f.append(s[i+1])
print(f)