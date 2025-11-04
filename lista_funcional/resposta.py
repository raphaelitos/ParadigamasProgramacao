# Questão 1
def head(lista):
    """Retorna o primeiro elemento de uma lista."""
    if lista == []:
        return None
    return lista[0]

# Questão 2
def tail(lista):
    """Retorna todos os elementos de uma lista, exceto o primeiro."""
    if lista == []:
        return None
    return lista[1:]

# Questão 3
def init(lista):
    """Retorna todos os elementos de uma lista, exceto o último."""
    if lista == []:
        return None
    inv = lista[::-1]
    cut = tail(inv)
    return cut[::-1]

# Questão 4
def last(lista):
    """Retorna o último elemento de uma lista."""
    if lista == []:
        return None
    inv = lista[::-1]
    return head(inv)

# Questão 5
def fibonacci(n):
    """Retorna o n-ésimo termo da sequência de Fibonacci."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Questão 6
def concat(l1, l2):
    """Concatena duas listas de forma recursiva."""
    if l1 == []:
        return l2
    if l2 == []:
        return l1
    
    listaconc = l1 + [head(l2)]
    return concat(listaconc, tail(l2))

# Questão 7
def inList(l1, item):
    """Verifica se um elemento pertence a uma lista."""
    if l1 == []:
        return False
    if head(l1) == item:
        return True
    
    nova_lista = tail(l1)
    return inList(nova_lista, item)

# Questão 8
def union(l1, l2):
    """Retorna a união de duas listas sem elementos repetidos."""
    if l2 == []:
        return l1
    
    item = head(l2)
    
    if inList(l1, item):
        return union(l1, tail(l2))
    else:
        return union(concat(l1, [item]), tail(l2))

# Questão 9
def upper_than_n(lista, n):
    """Conta quantos elementos da lista são maiores que n."""
    if(lista == []):
        return 0
    num = 0
    item = head(lista)
    
    if item > n:
        num = 1
    
    return num + upper_than_n(tail(lista), n)

# Questão 10
def upper_aux(lista, n, nova):
    """Função auxiliar que acumula elementos maiores que n."""
    if(lista == []):
        return nova

    item = head(lista)
    
    if item > n:
        return concat(upper_aux(tail(lista), n, nova), [item])
    else:
        return upper_aux(tail(lista), n, nova)

def upper_list(lista, n):
    """Retorna lista com elementos maiores que n."""
    if(lista == []):
        return []

    item = head(lista)
    
    if item > n:
        return concat(upper_aux(tail(lista), n, []), [item])
    else:
        return upper_aux(tail(lista), n, [])
    
def v2_upper_list(lista, n):
    """Retorna lista com elementos maiores que n."""
    if(lista == []):
        return []

    item = head(lista)
    
    if item > n:
        return concat([item], v2_upper_list(tail(lista), n))
    else:
        return v2_upper_list(tail(lista), n)
    

# Questão 11
def inverte_lista(lista):
    """Inverte o conteúdo de lista"""
    if(lista == []):
        return []
    return concat(inverte_lista(tail(lista)), [head(lista)])

#Questão 12
def gera_palindromo(palavra):
    """gera o palíndromo de palavra"""
    lista_pal = list(palavra) #transforma em lista
    inv = inverte_lista(lista_pal)
    
    return ''.join(concat(lista_pal, inv)) #transforma em string dnv


#Questão 13
def size_list(lista):
    """Retorna o tamanho de lista."""
    if(lista == []):
        return 0
    
    return 1 + size_list(tail(lista))

#Questão 14
from math import sqrt

def aux_eh_primo(num, div):
    if(div > sqrt(num)):
        return True
    
    if(num % div == 0):
        return False
    
    return aux_eh_primo(num, (div + 1))


def eh_primo(num):
    """Verifica se num é primo"""
    if (num <= 1):
        return False
    
    return aux_eh_primo(num, 2)

#Questão 15
def strip(l1, l2):
    """retira de l2 todos os elementos que ocorrem em l1"""
    if(l2 == []):
        return []
    
    item = head(l2)

    if(inList(l1, item)):
        return strip(l1, tail(l2))
    else:
        return concat([item], strip(l1, tail(l2)))

#Questão 16
def retira_vogal(lista):
    """retira todas as vogais de lista"""
    if(lista == []):
        return []
    
    vogais = list("aeiouAEIOU")
    item = head(lista)
    if(inList(vogais, item)):
        return retira_vogal(tail(lista))
    
    return concat([item], retira_vogal(tail(lista)))
    
def consoant_list(consoantes, palavra):
    """confere consoantes eh palavra sem vogal"""
    palavra_limpa = ''.join(retira_vogal(list(palavra)))

    return consoantes == palavra_limpa

#Questão 17


#Questão 18
def proximo_primo(num):
    """retorna o menor número primo que é maior que o número"""
    n = num + 1
    if(eh_primo(n)):
        return (n)
    
    return proximo_primo(n)


#Questão 19

#Questão 20


#--- testes ---#
l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l2 = [1, 2, 3, 4, 5, 6, 7, 8]
n = 24

print(consoant_list("brbr", "barbara"))