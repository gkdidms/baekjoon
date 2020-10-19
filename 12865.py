n, k = map(int, input().split())
aws = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1,n+1):   
    w, v = map(int, input().split())
    for j in range(1,k+1):  
        if w <= j:
            aws[i][j] = max(aws[i-1][j-w]+v,aws[i-1][j])
        else:
            aws[i][j] = aws[i-1][j]


print(aws[n][k])