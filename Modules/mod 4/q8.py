a=int(input('Ведите номер месяца '))
if a<=12:
    if a==2:
        print('28')
    elif a%2==1 and a<8:
        print('31')
    elif a%2==0 and a<8:
        print('30')
    elif a%2==0 and a>=8:
        print('31')
    else:
        print('30')
else:
    a = int(input('Ведите номер месяца'))