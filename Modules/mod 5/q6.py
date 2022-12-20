a=b=1
n=int(input())
c=[1,1]
while c[-1]<n:
    a,b=b,a+b
    c.append(b)
if c[-1]==n:
    print(len(c))
else:
    print(-1)




