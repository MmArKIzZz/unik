a=int(input())
b=int(input())
if b%2==0 and a%2==0 :
    print('черная')
elif b%2==0 and a%2==1:
    print('белая')
elif b%2==1 and a%2==0:
    print('белая')
elif b%2==1 and a%2==1:
    print('чёрная')
