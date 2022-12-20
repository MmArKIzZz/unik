a = input().split()
collection = {}
for b in a:
    c = collection.get(b, 0)
    print(c, end=" ")
    collection[b] = c + 1