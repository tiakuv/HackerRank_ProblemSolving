def diagonalDifference(arr):
    l = len(arr)
    res = 0
    res2 = 0
    
    for i in range(l):
        res += arr[i][i]
    
    j = l - 1
    for i in range(l):
        res2 += arr[i][j]
        j -= 1
    
    return abs(res-res2)