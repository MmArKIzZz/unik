a=1
c=1
d=[0]
m=0
while a!=0:
    a=int(input())
    if a==d[-1]:
        c+=1
        if m<c:
            m=c
    else:
        c=1
    d.append(a)
print(m)

