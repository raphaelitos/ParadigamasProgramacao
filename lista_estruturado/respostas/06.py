menor = maior = 0

for i in range(10):
    num = int(input())
    
    if i == 0:
       menor = maior = num

    if(num < menor):
        menor = num
    if(num > maior):
        maior = num

print(f"maior: {maior}, menor: {menor}")