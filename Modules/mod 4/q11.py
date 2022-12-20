a=int(input())
b=int(input())
y=int(input())
x=int(input())
c=0
v=0
if b%2==0 and a%2==0 :
    c=0
elif b%2==0 and a%2==1:
    c=1
elif b%2==1 and a%2==0:
    c=1
elif b%2==1 and a%2==1:
    c=0
if x%2==0 and y%2==0 :
    v=0
elif x%2==0 and y%2==1:
    v=1
elif x%2==1 and y%2==0:
    v=1
elif x%2==1 and y%2==1:
    v=0
if c==v:
    print('Да')
else:
    print('Нет')