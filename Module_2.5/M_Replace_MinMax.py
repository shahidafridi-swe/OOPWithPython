N = int(input())
lst = list(map(int, input().split()))

mx = max(lst)
mn = min(lst)
mxI = lst.index(mx)
mnI = lst.index(mn)

lst[mxI], lst[mnI] = lst[mnI], lst[mxI]
for x in lst:
        print(x, end=' ')