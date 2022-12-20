count = int(input())
names= {}
for _ in range(count):
    name, number = input().split()
    names[name] = int(number) + names.get(name, 0)
for key in sorted(names.keys()):
    print(key, names[key])
