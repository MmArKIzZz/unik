a=int(input())
b=int(input())
if a == 2:
    if b<28:
        print(f'{b+1}-{a}-2022')
    else:
        print(f'1-{a+1}-2022')
elif a % 2 == 1 and a < 8:
    if b<31:
        print(f'{b + 1}-{a}-2022')
    else:
        print(f'1-{a+1}-2022')
elif a % 2 == 0 and a < 8:
    if b < 30:
        print(f'{b + 1}-{a}-2022')
    else:
        print(f'1-{a + 1}-2022')
elif a % 2 == 0 and a >= 8:
    if b < 31:
        print(f'{b + 1}-{a}-2022')
    else:
        if a!=12:
            print(f'1-{a + 1}-2022')
        else:
            print('1-1-2023')
else:
    if b<30:
        print(f'{b + 1}-{a}-2022')
    else:
        print(f'1-{a+1}-2022')