def Lcs(a , b ):

    maxlcs = [[0 for i in range(len(b))] for i in range(len(a))]

    for j in range(m):
        if a[0] == b[j]:
            maxlcs[0][j] = 1
        elif j!=0:
            maxlcs[0][j] = maxlcs[0][j-1]
        else:
            maxlcs[0][j] = 0

    for i in range(n):
        if a[i] == b[0]:
            maxlcs[i][0] = 1
        elif i!=0:
            maxlcs[i][0] = maxlcs[i-1][0]
        else:
            maxlcs[i][0] = 0

    for i in range(1,n):
        for j in range(1,m):
            if a[i]==b[j]:
                maxlcs[i][j] = max(maxlcs[i-1][j] , maxlcs[i][j-1] , maxlcs[i-1][j-1]+1)
            else:
                maxlcs[i][j] = max(maxlcs[i-1][j] , maxlcs[i][j-1] , maxlcs[i-1][j-1])

    return maxlcs[n-1][m-1]
