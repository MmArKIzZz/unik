cities = {}
for _ in range(int(input())):
    cities_raw = input().split()
    for city in cities_raw[1:]:
        cities[city] = cities_raw[0]
output = []
for _ in range(int(input())):
    output.append(cities.get(input(), "Не найден"))
print("\n".join(output))
