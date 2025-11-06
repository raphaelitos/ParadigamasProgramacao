# só uma versao gepetonica usando funcoes builtin do python pra ver de quale. Não conferi se estão certas nem se eh tudo funcional mesmo

from functools import lru_cache
from itertools import groupby, chain
from math import sqrt
from collections import Counter

# Questão 1–4
def head(lst): """Retorna o primeiro elemento da lista."""; return lst[0] if lst else None
def tail(lst): """Retorna todos os elementos exceto o primeiro."""; return lst[1:] if lst else []
def init(lst): """Retorna todos os elementos exceto o último."""; return lst[:-1] if lst else []
def last(lst): """Retorna o último elemento da lista."""; return lst[-1] if lst else None

# Questão 5
@lru_cache(None)
def fibonacci(n): """Retorna o n-ésimo termo de Fibonacci."""; return n if n < 2 else fibonacci(n-1) + fibonacci(n-2)

# Questão 6
def concat(l1, l2): """Concatena duas listas."""; return l1 + l2

# Questão 7
def inList(lst, item): """Verifica se item pertence à lista."""; return item in lst

# Questão 8
def union(l1, l2): """Une duas listas sem repetições."""; return list(dict.fromkeys(l1 + l2))

# Questão 9
def upper_than_n(lst, n): """Conta elementos maiores que n."""; return sum(x > n for x in lst)

# Questão 10
def upper_list(lst, n): """Retorna elementos maiores que n."""; return [x for x in lst if x > n]

# Questão 11
def inverte_lista(lst): """Inverte a lista."""; return list(reversed(lst))

# Questão 12
def gera_palindromo(palavra): """Gera o palíndromo de uma palavra."""; return palavra + palavra[::-1]

# Questão 13
def size_list(lst): """Retorna o tamanho da lista."""; return len(lst)

# Questões 14, 18 e 19
def eh_primo(n, d=2):
    """Verifica se n é primo."""
    if n <= 1:
        return False
    if d > int(sqrt(n)):
        return True
    if n % d == 0:
        return False
    return eh_primo(n, d + 1)

def proximo_primo(n): 
    """Retorna o próximo número primo depois de n."""; 
    if eh_primo(n+1):
        return (n+1)
    return proximo_primo(n + 1)

def primes(num): 
    """Decompõe num em fatores primos."""
    if num in (0, 1): 
        return []
    
    def aux(n, div):
        if n == 1:
            return []
        if n % div == 0:
            return [div] + aux((n / div), div)
        
        return aux(n, proximo_primo(div))
    
    return aux(abs(num), 2)

# Questão 15
def strip(l1, l2): 
    """Remove de l2 os elementos contidos em l1."""; return [x for x in l2 if x not in l1]

# Questões 16–17
def retira_vogal(s): """Remove as vogais da string."""; return ''.join(ch for ch in s if ch.lower() not in 'aeiou')
def consoant_list(consoantes, palavra): """Verifica se palavra sem vogais = consoantes."""; return retira_vogal(palavra) == consoantes
def matches(palavras, consoantes): """Filtra palavras compatíveis com consoantes."""; return [p for p in palavras if consoant_list(consoantes, p)]

# Questão 20
def prime_factors(num): """Retorna pares (fator, frequência) da fatoração prima."""; return list(Counter(primes(num)).items())

# Questões 21–22
def split_token(token, lst): 
    """Divide lista em sublistas separadas por token."""
    result, temp = [], []
    for x in lst:
        if x == token:
            result.append(temp)
            temp = []
        else:
            temp.append(x)
    if temp: result.append(temp)
    return result

def join_token(token, mat): 
    """Une sublistas com token como separador."""
    return list(chain.from_iterable(sub + [token] for sub in mat))[:-1]

# Questão 23
def split_half(lst): """Divide lista em duas metades."""; i = len(lst)//2; return [lst[:i], lst[i:]]

# Questão 24
def pyths(n): """Retorna triplas pitagóricas com lados até n."""; return [(x,y,z) for x in range(1,n+1) for y in range(1,n+1) for z in range(1,n+1) if x*x + y*y == z*z]

# Questões 25
def fatores(num): """Retorna os divisores de num."""; return [i for i in range(1, abs(num)//2 + 1) if num % i == 0]
def soma(lst): """Soma os elementos da lista."""; return sum(lst)
def eh_perfeito(num): """Verifica se num é perfeito."""; return num == soma(fatores(num))
def perfects(n): """Retorna números perfeitos até n."""; return [x for x in range(1, n+1) if eh_perfeito(x)]

# Questão 26
def escalar(v, w): """Calcula produto escalar entre v e w."""; return sum(a*b for a,b in zip(v,w))

# Questão 27
def ataca(p, posicoes, n=8): 
    """Verifica se a rainha p ataca alguma posição."""
    a,b = p
    ataques = {(x,y) for x in range(1,n+1) for y in range(1,n+1)
               if x==a or y==b or abs(x-a)==abs(y-b)}
    return any(pos in ataques for pos in posicoes)

# Questão 28
def is_palindrome(palavra): """Verifica se palavra é palíndromo."""; return palavra == palavra[::-1]

# Questões 29–30
def compress(lst): """Remove duplicatas consecutivas."""; return [k for k,_ in groupby(lst)]
def pack(lst): """Agrupa duplicatas consecutivas."""; return [list(g) for _,g in groupby(lst)]

# Questão 31
def encode(palavra): """Codifica palavra por run-length."""; return [(ch, len(list(g))) for ch,g in groupby(palavra)]

# Questão 32
def decode(lista_code): """Decodifica lista run-length."""; return ''.join(ch * n for ch,n in lista_code)


print(primes(28))