vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

strCount = input()
count = 0

for letra in strCount:
    if letra in vogais:
        count+=1

print(count)