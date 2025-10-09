def confere_vet(vet):
    flags = [False, False, False, False, False, False, False, False, False, False]
    for i in range(9):
        
        if((not(0 <= vet[i] <= 9)) or flags[i]):
            return False
        
        flags[i] = True

def confere_mat(mat):
    flags = [[False, False, False], [False, False, False], [False, False, False]]
    for i in range(3):
        for j in range(3):

            if(((not(0 <= mat[i][j] <= 9)) or (not(0 <= i <= 9))) or flags[i][j]):
                return False
        
        flags[i][j] = True
    