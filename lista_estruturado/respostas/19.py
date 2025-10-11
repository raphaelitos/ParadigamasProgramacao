'''
def confere_vet(vet):
    flags = [False, False, False, False, False, False, False, False, False]
    for i in range(9):
        
        if(9 < vet[i] < 1 or flags[vet[i] - 1]):
            return False
        
        flags[vet[i] - 1] = True

def confere_mat_3x3(mat):
    flags = [[False, False, False], [False, False, False], [False, False, False]]
    for i in range(3):
        for j in range(3):

            if(((not(0 < mat[i][j] <= 9)) or (not(0 <= i <= 9))) or flags[i][j]):
                return False
        
        flags[i][j] = True
'''

def corrige_sudoku(mat):
    gabaritoLinhas = [[False, False, False, False, False, False, False, False, False]
                [False, False, False, False, False, False, False, False, False]
                [False, False, False, False, False, False, False, False, False]
                [False, False, False, False, False, False, False, False, False]
                [False, False, False, False, False, False, False, False, False]
                [False, False, False, False, False, False, False, False, False]
                [False, False, False, False, False, False, False, False, False]
                [False, False, False, False, False, False, False, False, False]
                [False, False, False, False, False, False, False, False, False]]
    
    gabaritoColunas = [[False, False, False, False, False, False, False, False, False]
                [False, False, False, False, False, False, False, False, False]
                [False, False, False, False, False, False, False, False, False]
                [False, False, False, False, False, False, False, False, False]
                [False, False, False, False, False, False, False, False, False]
                [False, False, False, False, False, False, False, False, False]
                [False, False, False, False, False, False, False, False, False]
                [False, False, False, False, False, False, False, False, False]
                [False, False, False, False, False, False, False, False, False]]
    

    gabaritoQuadrados = [[False, False, False, False, False, False, False, False, False]
                [False, False, False, False, False, False, False, False, False]
                [False, False, False, False, False, False, False, False, False]
                [False, False, False, False, False, False, False, False, False]
                [False, False, False, False, False, False, False, False, False]
                [False, False, False, False, False, False, False, False, False]
                [False, False, False, False, False, False, False, False, False]
                [False, False, False, False, False, False, False, False, False]
                [False, False, False, False, False, False, False, False, False]]
    

    for i in range(9):
        
        for j in range(9):
            if(9 < mat[i][j] < 1 or gabaritoLinhas[i][j]:
                return False