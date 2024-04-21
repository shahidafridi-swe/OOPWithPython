n = int(input())
lst = list(map(int, input().split()))

lst2 = lst.copy()
lst2.reverse()
print("YES" if lst == lst2 else "NO")

