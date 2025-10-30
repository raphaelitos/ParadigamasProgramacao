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

# Questão 7
def inList(l1, item):
    if l1 == []:
        return False
    if head(l1) == item:
        return True
    
    nova_lista = tail(l1)
    return inList(nova_lista, item)

# Questão 8
def union(l1, l2):
    if l1 == []:
        return l2
    if l2 == []:
        return l1
    
    item = head(l2)
    listaconc = l1
    
    if not inList(l1, item):
        listaconc = l1 + [item]
    
    return union(listaconc, tail(l2))

# Questão 9
def upper_than_n(lista, n):
    if(lista == []):
        return 0
    num = 0
    item = head(lista)
    
    if item > n:
        num = 1
    
    return num + upper_than_n(tail(lista), n)


def upper_aux(lista, n, nova):
    if(lista == []):
        return nova

    item = head(lista)
    
    if item > n:
        return concat(upper_aux(tail(lista), n, nova), [item])
    else:
        return upper_aux(tail(lista), n, nova)

# Questão 10
def upper_list(lista, n):
    if(lista == []):
        return []

    item = head(lista)
    
    if item > n:
        return concat(upper_aux(tail(lista), n, []), [item])
    else:
        return upper_aux(tail(lista), n, [])
    

l1 = [1, 2, 3, 4, 5]
l2 = [8, 16, 32, 64, 128]
n = 14


print(upper_list(l2, n))