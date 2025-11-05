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
        return []
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
    if (num == 1 or num == 0):
        return False
    if(num < 0):
        return aux_eh_primo((num * (-1)), 2)
    
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
    
    return strip(vogais, lista)
    
def consoant_list(consoantes, palavra):
    """confere se consoantes eh palavra sem vogal"""
    palavra_limpa = ''.join(retira_vogal(list(palavra)))

    return consoantes in palavra_limpa

#Questão 17
def matches(palavras, consoantes):
    """retorna os itens em palavras onde consoantes eh o item sem vogal"""
    if(palavras == []):
        return []
    
    item = head(palavras)
    
    if(consoant_list(consoantes, item)):
        return concat([item], matches(tail(palavras), consoantes))

    return matches(tail(palavras), consoantes)

#Questão 18
def proximo_primo(num):
    """retorna o menor número primo que é maior que num"""
    n = num + 1
    if(eh_primo(n)):
        return (n)
    
    return proximo_primo(n)

#Questão 19
def primes_aux(num, div):
    if (num == 1):
        return []
    if((num % div) == 0):
        return concat([div], primes_aux((num/div), div))
    else:
        return primes_aux(num, proximo_primo(div))

def primes(num):
    """Decompoe num em fatores primos"""
    if (num == 0):
        return []
    if(num < 0):
        return primes_aux((num * (-1)), 2)
    
    return primes_aux(num, 2)

#Questão 20
def count(lista, item):
    """Conta quantas vezes item aparece em lista."""
    if lista == []:
        return 0
    if head(lista) == item:
        return 1 + count(tail(lista), item)
    else:
        return count(tail(lista), item)
    
def prime_fac_aux(decomposicao):
    """Gera lista de pares (fator, frequência) a partir de uma lista ordenada de fatores primos."""
    if decomposicao == []:
        return []
    
    item = head(decomposicao)
    freq = count(decomposicao, item)
    nova_decomposicao = strip([item], decomposicao)
    
    return concat([(item, freq)], prime_fac_aux(nova_decomposicao))

def prime_factors(num):
    """Fatora num em pares (fator, frequência)."""
    if(num == 0):
        return []
    
    decomposicao = primes(num)

    return prime_fac_aux(decomposicao)


# Questão 21
def split_aux(token, lista):
    """Retorna a primeira fatia de lista delimitada por token."""
    if(lista == [] or head(lista) == token):
        return []
    
    return concat([head(lista)], split_aux(token, tail(lista)))

def split_token(token, lista):
    "Reparte lista em sublistas delimitadas por token."
    if(lista == []):
        return []

    tok_list = split_aux(token, lista)
    resto = lista[size_list(tok_list):]

    return concat([tok_list], split_token(token, tail(resto)))

#Questão 22
def join_token(token, mat):
    """Une as linhas de mat usando token como separador."""
    if(size_list(mat) == 1):
        return [token] + head(mat)
    
    if(size_list(mat) == 0):
        return []
    
    conc = head(mat) + [token]
    novo_item = concat(conc, head(tail(mat)))

    return concat(novo_item, join_token(token, tail(tail(mat))))

#Questão 23
#definindo as proximas duas para nao usar slice
def take_n(n, lista):
        """Retorna os n primeiros elementos de lista."""
        if (n == 0 or lista == []):
            return []
        return concat([head(lista)], take_n(n - 1, tail(lista)))

def drop_n(n, lista):
    """Descarta os n primeiros elementos de lista"""
    if (n == 0 or lista == []):
        return lista
    return drop_n((n - 1), tail(lista))

def split_half(lista):
    """Retorna uma lista com duas sublistas correspondendo às metades de lista"""
    if(lista == []):
        return [[], []]
    
    i = size_list(lista)//2
    a = take_n(i, lista)
    b = drop_n(i, lista)
    
    return [a, b]

#Questão 24
def pyths(n):
    """Retorna todas as triplas pitagóricas (x, y, z) com 1 <= x, y, z <= n."""
    return [(x, y, z)
            for x in range(1, n + 1)
            for y in range(1, n + 1)
            for z in range(1, n + 1)
            if x * x + y * y == z * z]

#Questão 25
def fatores_aux(num, div):
    if ((num/2) < div):
        return []
    if((num % div) == 0):
        return concat([div], fatores_aux(num, (div + 1)))
    else:
        return fatores_aux(num, (div + 1))

def fatores(num):
    """Retorna os fatores de num"""
    if (-1 <= num <= 1):
        return []
    if(num < 0):
        return fatores_aux((num * (-1)), 2)
    
    return [1] + fatores_aux(num, 2)

def soma(lista):
    """Soma os elementos de lista"""
    if(lista == []):
        return 0
    
    return head(lista) + soma(tail(lista))

def eh_perfeito(num):
    return num == soma(fatores(num))


def perfects(n):
    """Retorna a lista de numeros perfeitos em [1, n]"""
    return [
        x
        for x in range(1, n+1)
        if eh_perfeito(x)
    ]

#Questão 26
def escalar(v, w):
    """Calcula o produto escalar entre v e w"""
    if(size_list(v) != size_list(w)):
        return 0
    #zip emparelha os itens de v e w par a par
    return soma([x * y for x, y in zip(v, w)])

#Questão 27
def is_some_in(l1, l2):
    """Verifica se há algum item de l1 em l2"""
    if(l1 == []):
        return False
    
    if inList(l2, head(l1)):
        return True
    
    return is_some_in(tail(l1), l2)

def ataca(p, posicoes):
    """verifica se a rainha na posicao p ataca alguma em posicoes"""
    ataques_rainha = [
            (a, b)
            for a in range(1, 8 + 1)
            for b in range(1, 8 + 1)
            if(
                (a == p[0]) or #linhas
                (b == p[1]) or #colunas
                (abs(a - p[0]) == abs(b - p[1])) #diagonais
            )
        ]
    
    return is_some_in(posicoes, ataques_rainha)


#Questão 28
def is_palindrome(palavra):
    """Verifica se palavra eh um palindromo"""
    l = list(palavra)
    half_mat = split_half(l)
    
    if(size_list(l) % 2 == 0):
        return half_mat[0] == inverte_lista(half_mat[1])
    
    return half_mat[0] == inverte_lista(tail(half_mat[1]))


#Questão 29
def compress(lista):
    """Elimina duplicatas em lista"""
    if(lista == []):
        return []
    if(size_list(lista) == 1):
        return lista
    
    a = lista[0]
    b = lista[1]

    if(a == b):
        return compress(tail(lista))
    
    return concat([a], compress(tail(lista)))

    
#Questão 30
def take_while_equal(x, lista):
    """Coleta em lista os elementos consecutivos a x iguais a ele"""
    if lista == [] or head(lista) != x:
        return []
    return concat([head(lista)], take_while_equal(x, tail(lista)))

def drop_while_equal(x, lista):
    """Remove de lista os elementos consecutivos a x iguais a ele"""
    if lista == [] or head(lista) != x:
        return lista
    return drop_while_equal(x, tail(lista))

def pack(lista):
    """Empacota duplicatas contidas em lista"""
    if lista == []:
        return []
    
    atual = head(lista)
    grupo = take_while_equal(atual, lista)
    resto = drop_while_equal(atual, lista)
    
    return concat([grupo], pack(resto))


# Questão 31
def aux_encode(lista_code):
    if(size_list(lista_code) == 0):
        return []

    item = head(lista_code)
    code = size_list(item)
    
    return concat([(head(item), code)], aux_encode(tail(lista_code)))

def encode(palavra):
    code = pack(list(palavra))
    return aux_encode(code)


# Questão 32
def decode(lista_code):
    if(lista_code == []):
        return ''
    
    item = head(lista_code)

    return (item[0] * item[1]) + decode(tail(lista_code))

#--- testes ---#
l1 = [1,2,2, 2, 2, 3, 3, 4, 5]
l2 = [1, 2, 3,1, 4, 5, 1, 6, 7, 1, 8]
l3 = [[10], [20,30], [40]]
n = 24
dic = ["arara","arreio","haskell","vaca","vacuo","velho","vermelho","vicio"]

print(matches (dic, "rr"))