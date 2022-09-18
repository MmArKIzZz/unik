n=int(input())
if n//60<10:
    print(f'{n // 60}:0{n - (n // 60) * 60}')
else:
    print(f'{n//60}:{n-(n//60)*60}')