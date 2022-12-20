count = int(input())
syn= dict([input().split() for _ in range(count)])
a = input()
for key, value in syn.items():
    if a == key:
        print(value)
    elif a == value:
        print(key)
    else:
        continue
    break
