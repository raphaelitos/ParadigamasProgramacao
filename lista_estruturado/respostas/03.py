size = 5
numbers = []
swap = False

for i in range(size):
    num = int(input())
    numbers.append(num)

for m in range(size):
    swap = False
    for n in (range(size - m - 1)):
        if(numbers[n] > numbers[n + 1]):
            aux = numbers[n]
            numbers[n] = numbers[n + 1]
            numbers[n + 1] = aux
            swap = True

    if(swap == False):
        break

print(numbers)