b=int(input())
c=0
while b!=0:
    a=int(input())
    if a==0:
        break
    elif b<a:
        c+=1
    else:
        c=0
        b=a
print(c)
