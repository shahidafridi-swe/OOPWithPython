N, Q = map(int, input().split())
A = list(map(int, input().split()))
for q in range (Q):
    L, R = map(int, input().split())
    result = 0
    
    for i in range(L-1,R):
        result += A[i]
    print(result)