T = int(input())

for t in range(T):
    n = int(input())

    lst = list(map(int, input().split()))
    result = []
    for i in range (1,n):
        for j in range(i+1, n+1):
            x = lst[i-1]+lst[j-1]+j-i
            result.append(x)
    print(min(result))