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
            if(9 < mat[i][j] < 1 or gabaritoLinhas[i][j]):
                return False