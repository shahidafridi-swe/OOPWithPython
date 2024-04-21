n = int(input())
A = list(map(int,input().split()))
flag = True
cnt = 0
while flag:
    for i in range(n):
        if(A[i] %2 != 0):
            flag = False
            break
    if flag:
        for i in range(n):
            A[i] = A[i]/2 
        cnt +=1
    
print(cnt)


