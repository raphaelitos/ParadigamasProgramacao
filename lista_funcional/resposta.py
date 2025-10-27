# Questão 1
def head(lista):
    if lista == []:
        return None
    return lista[0]

# Questão 2
def tail(lista):
    if lista == []:
        return None
    return lista[1:]

# Questão 3
def init(lista):
    if lista == []:
        return None
    inv = lista[::-1]
    cut = tail(inv)
    return cut[::-1]

# Questão 4
def last(lista):
    if lista == []:
        return None
    inv = lista[::-1]
    return head(inv)

# Questão 5
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Questão 6
def concat(l1, l2):
    if l1 == []:
        return l2
    if l2 == []:
        return l1
    
    listaconc = l1 + [head(l2)]
    return concat(listaconc, tail(l2))

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
print(concat(l1, l2))