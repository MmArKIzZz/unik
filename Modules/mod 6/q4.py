numbers: list[int] = [int(x) for x in input().split()]
min= numbers.index(min(numbers))
max = numbers.index(max(numbers))

numbers[min], numbers[max] = (numbers[max], numbers[min],)
print(" ".join(map(str, numbers)))