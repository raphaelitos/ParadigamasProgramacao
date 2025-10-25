def confere_digito(d):
    return 0 < d <= 9

def confere_vet(vet):
    flags = [False, False, False, False, False, False, False, False, False]
    for i in range(9):
        pos = vet[i] - 1
        if(not(confere_digito(vet[i])) or flags[pos]):
            return False
        
        flags[pos] = True
    return True


def confere_mat_3x3(mat):
    flags = [[False, False, False], [False, False, False], [False, False, False]]
    
    for i in range(3):
        for j in range(3):
            digito = mat[i][j]
            linha = (digito - 1) // 3
            coluna = (digito - 1) % 3
            if(not(confere_digito(digito)) or flags[linha][coluna]):
                return False
        
            flags[linha][coluna] = True
    
    return True

def confere_sudoku(mat):
    # Linhas
    for i in range(9):
        if not confere_vet(mat[i]):
            return False

    # Colunas
    for j in range(9):
        coluna = []
        for i in range(9):
            coluna.append(mat[i][j])
        if not confere_vet(coluna):
            return False

    # Submatrizes 3x3
    for li in range(0, 9, 3):
        for cj in range(0, 9, 3):
            submat = []
            for i in range(3):  # linhas do bloco
                linha = []
                for j in range(3):  # colunas do bloco
                    linha.append(mat[li + i][cj + j])
                submat.append(linha)
            if not confere_mat_3x3(submat):
                return False

    return True