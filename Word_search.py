def pattern(mat, word, x, y, n, m, wlen, wIdx):
    if wlen == wIdx:
        return True
    
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
        
    if mat[x][y] == word[wIdx]:
        temp = mat[x][y]
        mat[x][y] = '#'
        
        res = (pattern(mat, word, x - 1, y, n, m, wlen, wIdx + 1) or pattern(mat, word, x + 1, y, n, m, wlen, wIdx + 1) or
        pattern(mat, word, x, y + 1, n ,m ,wlen, wIdx + 1) or pattern(mat, word, x, y - 1, n, m, wlen, wIdx + 1))
        
        mat[x][y] = temp
        return res
    return False
    
def isWordExist(mat, word):
    n = len(mat)
    m = len(mat[0])
    wlen = len(word)
    
    for i in range(n):
        for j in range(m):
            if mat[i][j] == word[0]:
                if pattern(mat, word, i, j, n, m, wlen, 0):
                    return True
    return False
  
mat = [['T', 'E', 'E'], ['S', 'G', 'K'], ['T', 'E', 'L']]
word = "GEEK"
print("true" if isWordExist(mat, word) else "false")
